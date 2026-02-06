# X/Twitter Algorithm Deep Dive: Complete Technical Research

**Research Date:** February 6, 2026
**Sources:** GitHub open-source code (twitter/the-algorithm, xai-org/x-algorithm), X Engineering Blog, independent analyses of 18M+ posts, and multiple technical breakdowns.

---

## Table of Contents

1. [Algorithm Architecture Overview](#1-algorithm-architecture-overview)
2. [Ranking Signals That Boost Distribution](#2-ranking-signals-that-boost-distribution)
3. [Signals That Kill Distribution](#3-signals-that-kill-distribution)
4. [The "For You" Feed: How It Actually Works](#4-the-for-you-feed-how-it-actually-works)
5. [Engagement Type Weights (From the Source Code)](#5-engagement-type-weights-from-the-source-code)
6. [Recent Algorithm Changes (2025-2026)](#6-recent-algorithm-changes-2025-2026)
7. [Key Technical Details From the Open-Source Code](#7-key-technical-details-from-the-open-source-code)
8. [Tactical Implications](#8-tactical-implications)
9. [Sources](#9-sources)

---

## 1. Algorithm Architecture Overview

X's recommendation algorithm has gone through two major eras:

### Era 1: Legacy System (Open-sourced March 2023)

- **Repository:** `twitter/the-algorithm` and `twitter/the-algorithm-ml`
- **Framework:** Custom Scala framework called "Product Mixer"
- **Orchestration:** "Home Mixer" service constructs and serves the For You timeline
- **ML Model:** Parallel MaskNet architecture (the "Heavy Ranker")

### Era 2: Grok-Powered System (Open-sourced January 20, 2026)

- **Repository:** `xai-org/x-algorithm`
- **Framework:** Rust-based codebase
- **Architecture:** Four core components:
  - **Home Mixer** -- Orchestration layer; exposes gRPC endpoint returning ranked posts per user
  - **Thunder** -- In-memory post store; sub-millisecond lookups for in-network content; consumes Kafka events for post creation/deletion
  - **Phoenix** -- Grok-based transformer model for ML ranking (retrieval + ranking)
  - **Candidate Pipeline** -- Reusable trait-based architecture for sourcing, hydrating, filtering, scoring, selecting candidates
- **Scale:** Processes approximately 5 billion ranking decisions per day; each decision requires 220 seconds of CPU time but completes in under 1.5 seconds

### The Three-Stage Pipeline (Both Eras)

**Stage 1: Candidate Retrieval**

- Fetches approximately 1,500 candidate tweets from hundreds of millions of posts
- Split roughly 50/50 between in-network (followed accounts) and out-of-network content
- In-network: Ranked by "Real Graph" -- a model predicting engagement likelihood between two specific users
- Out-of-network: Surfaced through SimClusters (145,000 topic communities, updated every 3 weeks) and GraphJet (real-time interaction graph traversals serving ~15% of timeline tweets)

**Stage 2: Machine Learning Ranking**

- A neural network analyzes thousands of features per tweet
- Outputs probability predictions for 15+ engagement types
- Combines predictions into a weighted score

**Stage 3: Heuristics & Filtering**

- Pre-scoring filters: duplicates, age thresholds, self-posts, blocked/muted authors, muted keywords, previously seen posts
- Post-selection filters: visibility filtering (deleted, spam, violence), conversation thread deduplication
- Diversity mechanisms: Author Diversity Scorer attenuates repeated authors; OON Scorer adjusts out-of-network content balance

---

## 2. Ranking Signals That Boost Distribution

### Primary Positive Signals (Ranked by Weight)

| Signal                           | Code Weight | Multiplier vs. Like | Description                                                              |
| -------------------------------- | ----------- | ------------------- | ------------------------------------------------------------------------ |
| **Reply engaged by author**      | +75.0       | **150x**            | A reply to your tweet that YOU then engage with (reply back, like, etc.) |
| **Reply**                        | +13.5       | **27x**             | Someone replies to your tweet                                            |
| **Good profile click**           | +12.0       | **24x**             | User opens your profile and then likes or replies to something           |
| **Good click (engagement)**      | +11.0       | **22x**             | User clicks into the conversation and engages                            |
| **Good click v2 (dwell 2+ min)** | +10.0       | **20x**             | User clicks into the conversation and stays for 2+ minutes               |
| **Bookmark**                     | ~+10.0      | **20x**             | User bookmarks your tweet                                                |
| **Retweet**                      | +1.0        | **2x**              | User retweets your tweet                                                 |
| **Favorite (Like)**              | +0.5        | **1x** (baseline)   | User likes your tweet                                                    |
| **Video playback 50%**           | +0.005      | negligible          | User watches 50%+ of video content                                       |

**The critical insight:** Conversation depth dominates everything. One genuine reply chain where the author engages back is worth more than hundreds of likes.

### Secondary Positive Signals

- **Engagement velocity:** How quickly interactions accumulate in the first 30 minutes (the "critical engagement window")
- **Dwell time:** Text posts where people stay for 2+ seconds receive algorithmic boosts
- **Real Graph score:** Historical engagement pattern between the viewer and the poster; higher scores mean higher likelihood of appearing in feed
- **Recency:** Freshness of content heavily weighted; the algorithm prioritizes recent tweets
- **Media richness:** Images, videos, GIFs, and polls receive algorithmic boosts over plain text
- **Topic relevance:** Semantic alignment with user interests via SimClusters matching (cosine similarity >= 0.7 in production triggers relevance)
- **Trending conversation participation:** Alignment with current trending topics boosts visibility

### Engagement Multipliers (Simplified Formula)

An alternative representation used in some analyses:

| Action         | Simplified Multiplier |
| -------------- | --------------------- |
| Likes          | 1x (baseline)         |
| Retweets       | 20x                   |
| Quote Tweets   | 15x                   |
| Replies        | 13.5x                 |
| Profile Clicks | 12x                   |
| Link Clicks    | 11x                   |
| Bookmarks      | 10x                   |

---

## 3. Signals That KILL Distribution

### Negative Signals (From the Source Code)

| Signal                   | Code Weight | Impact                                                                          |
| ------------------------ | ----------- | ------------------------------------------------------------------------------- |
| **Report**               | **-369.0**  | User reports tweet as spam/abuse/misinfo; essentially removes from distribution |
| **Negative feedback v2** | **-74.0**   | User clicks "show less often," blocks, or mutes                                 |

### Distribution Killers in Practice

**External Links:**

- 30-50% reach penalty for any external link (up from 20-30% in 2023-2024)
- Facebook/Instagram links: additional -60% penalty on top
- Multiple links per tweet: -70% penalty
- Since March 2025: Non-Premium accounts posting links receive **zero median engagement** -- their link posts are essentially invisible
- Case study: 1,700% reach increase when removing a link from an identical tweet

**Community Notes:**

- Tweets flagged with Community Notes: immediate -60% to -80% reach reduction
- Excluded entirely from the "For You" feed
- Limited to chronological follower feeds only
- Recovery time: 7-14 days

**Hashtag Overuse:**

- 3+ hashtags: up to -40% penalty
- Optimal: 1-2 relevant, niche hashtags (+21% engagement)

**Negative/Combative Tone:**

- Grok's sentiment analysis (introduced late 2025) now monitors tone of every post
- Negative or combative messaging receives reduced distribution even if engagement is high
- Positive/constructive messaging receives wider distribution

**All-Caps Text:**

- Penalized by the algorithm

**Mass Unfollowing:**

- Can trigger a 3-month shadowban

**Engagement Debt:**

- Accounts with high post volume but low per-tweet engagement rates are penalized
- Better to post 10 high-quality tweets than 30 mediocre ones

### Shadowban Durations

- First-time offense: 48-72 hours
- Repeat violations: 7-14 days
- Mass unfollowing: 3 months

---

## 4. The "For You" Feed: How It Actually Works

### Candidate Sourcing (Getting Into the Pool)

**In-Network Sources (~50% of candidates):**

- Tweets from accounts you follow
- Ranked primarily by **Real Graph** -- a directed, weighted graph modeling user relationships
- Real Graph edge features: days since edge creation, days since last interaction, number of common friends, engagement statistics (explicit and implicit)
- Served from Thunder's in-memory store for sub-millisecond lookups

**Out-of-Network Sources (~50% of candidates):**

1. **SimClusters** -- Primary discovery mechanism
   - 145,000 overlapping communities discovered via custom matrix factorization
   - Updated every 3 weeks
   - Each user has a "KnownFor" vector (what communities they produce for) and an "InterestedIn" vector (computed from who they follow)
   - Tweet embeddings updated each time a post is favorited -- the InterestedIn vector of the favoriting user is added to the post vector
   - Cosine similarity >= 0.7 triggers relevance match

2. **GraphJet** -- Graph-based discovery
   - Real-time interaction graph processing engine
   - Traverses engagement and follow networks
   - Serves ~15% of Home Timeline tweets

3. **Phoenix Retrieval** (2026 system) -- Two-tower architecture
   - User tower encodes engagement history into embeddings
   - Candidate tower encodes all posts into embeddings
   - Top-K retrieval via dot product similarity search

### Ranking (Scoring Each Candidate)

**Legacy System (Heavy Ranker):**

- Parallel MaskNet architecture
- Outputs 10 probability predictions (0 to 1) per tweet
- Weighted sum produces final score

**Current System (Phoenix Ranking):**

- Grok-based transformer model
- "Candidate isolation" -- candidates cannot attend to each other during inference, only to user context
- Outputs probabilities for 15+ engagement actions simultaneously
- No hand-engineered features -- the transformer learns entirely from engagement sequences
- Multi-stage scoring: Phoenix Scorer -> Weighted Scorer -> Author Diversity Scorer -> OON Scorer

### Filtering & Blending

- Author diversity enforcement (prevents timeline domination by one account)
- Content type balancing
- Duplicate removal and conversation thread deduplication
- Blocked/muted/hidden content removal
- Policy-based filters (spam, violence, gore)

---

## 5. Engagement Type Weights (From the Source Code)

### Original Open-Source Weights (April 5, 2023 -- twitter/the-algorithm-ml)

These are the exact configuration values from the GitHub commit:

```
scored_tweets_model_weight_fav: 0.5
scored_tweets_model_weight_retweet: 1.0
scored_tweets_model_weight_reply: 13.5
scored_tweets_model_weight_good_profile_click: 12.0
scored_tweets_model_weight_good_click: 11.0
scored_tweets_model_weight_good_click_v2: 10.0
scored_tweets_model_weight_video_playback50: 0.005
scored_tweets_model_weight_reply_engaged_by_author: 75.0
scored_tweets_model_weight_negative_feedback_v2: -74.0
scored_tweets_model_weight_report: -369.0
```

**How to read this:** These weights are multiplied by the predicted probability of each action. A tweet where the model predicts a 10% chance of reply (weight 13.5) scores 1.35 from that signal alone, while a 10% chance of favorite (weight 0.5) scores only 0.05.

**Design principle:** The weights were originally calibrated so that each weighted engagement probability contributed near-equal amounts to the overall score on average. This means the seemingly large weight on replies (13.5) reflects that replies are rarer than likes, so the higher weight normalizes their contribution.

### 2026 System (xai-org/x-algorithm)

The Phoenix model predicts probabilities for:

- Favorites, replies, reposts, quotes, clicks, profile clicks
- Video views, photo expansions, shares, dwell time
- Follow author
- Negative actions: not_interested, block, mute, report

The weighted scoring formula remains: **Final Score = SUM(weight_i x P(action_i))**

Specific weight values for the new system have not been published in the open-source release, but the architecture confirms that positive weights apply to favorable actions and negative weights apply to rejection signals, following the same principle as the legacy system.

---

## 6. Recent Algorithm Changes (2025-2026)

### October 2025: Grok Announcement

- Elon Musk announced that Grok would replace the legacy recommendation system entirely
- "Grok will literally read every post and watch every video (100M+ per day) to match users with content they're most likely to find interesting"
- Goal: Deletion of all manual heuristics within 4-6 weeks

### November 2025: Following Feed Changes

- The "Following" feed became Grok-sorted by default (previously chronological)
- Users can toggle back to chronological order
- Ranked based on past interactions, topic engagement, and followed account signals

### January 20, 2026: New Algorithm Open-Sourced

- xAI released the Grok-powered algorithm code at `xai-org/x-algorithm`
- 1,600 GitHub stars within six hours
- Rust-based codebase replaces Scala-based legacy system
- Commits to update every four weeks with detailed developer notes
- Apache License 2.0

### February 2026: Communities Go Public

- Community posts now visible to everyone (not just members)
- Community content surfaces in the "For You" feed

### Key Behavioral Changes

**Sentiment Analysis (New):**

- Grok monitors the tone of every post
- Positive/constructive messaging gets wider distribution
- Negative/combative tone gets reduced visibility EVEN IF engagement metrics are high
- This represents a fundamental shift from pure engagement optimization

**Natural Language Feed Customization (New):**

- Users can input commands like "Show me more tech innovations, less politics"
- Grok interprets these to personalize the feed

**Premium vs. Free Gap (Widening):**

- Premium accounts: ~10x more reach per post than free accounts
- Premium in-network visibility: 4x boost
- Premium out-of-network visibility: 2x boost
- Free accounts: 10-20% of followers see initial tweets
- Premium accounts: 40-80% of followers see initial tweets
- Premium+ delivers the strongest visibility boost of all tiers

**Link Penalty (Increasing):**

- 2023-2024: 20-30% reach reduction for links
- 2025-2026: 30-50% reach reduction for links
- March 2025 onward: Non-Premium link posts show zero median engagement

### Content Format Performance (2025-2026 Data)

**Unique to X: Text outperforms video**

- Text-only posts: 30% more engagement than video (X is the ONLY major platform where this is true)
- Video: 5.4% more engagement than images
- Images: 12% more engagement than links
- Links: Essentially dead for free accounts

**Video Specifications When Used:**

- Optimal length: 15-60 seconds
- Preferred format: 9:16 vertical
- Completion rate: 50%+ triggers additional boost
- Native upload strongly preferred over external links (YouTube, etc.)
- Maximum effective length: under 2:20

**Thread Performance:**

- 3-5 tweet threads: 40-60% more total impressions than the equivalent standalone tweets
- Thread completion rate target: 70-80%
- The initial tweet receives standard distribution; subsequent tweets are primarily shown to users who engaged with the first tweet
- Threads demonstrate expertise and increase dwell time

**Long-Form Content:**

- Available only to Premium subscribers (up to 25,000 characters)
- No confirmed algorithmic advantage for long-form over threads or single tweets
- The advantage is dwell time -- longer reads naturally increase the dwell signal

---

## 7. Key Technical Details From the Open-Source Code

### TweepCred: The Hidden Reputation Score

**What it is:** A 0-100 credibility/reputation score assigned to every X account, not displayed publicly.

**How it works:**

- Based on a weighted PageRank algorithm (adapted from Google's web page ranking)
- Creates a graph of users (nodes) and interactions (edges)
- Assigns numerical scores based on the number and quality of interactions

**Key Factors:**

- Follower-to-following ratio (balanced ratios signal authenticity)
- Engagement quality (consistent likes, replies, reposts from reputable users)
- Account age and activity (older, active accounts score higher)
- Network quality (who engages with you matters)

**Impact:**

- Below the critical threshold of 65: Only 3 of your tweets are considered for algorithmic distribution
- A high score can amplify reach by up to 50x
- A low score leads to throttling where posts barely get visibility
- Premium subscribers receive a +4 to +16 point boost to their TweepCred
- New accounts start low and build over time through positive interactions
- Most healthy accounts fall between 30-75

### Real Graph: Predicting User-to-User Engagement

- Directed, weighted graph modeling user relationships
- Nodes = users; edges = follow/contact/interaction relationships
- Edge features: days since creation, days since last interaction, common friends count, engagement statistics
- A higher Real Graph score between viewer and poster = higher probability of that tweet appearing in the viewer's feed
- This is why consistently engaging with specific accounts causes more of their content to appear

### SimClusters: Topic/Interest Matching

- 145,000 overlapping communities via custom matrix factorization
- Updated every 3 weeks
- Two matrices: "KnownFor" (what you produce) and "InterestedIn" (what you consume)
- InterestedIn = Follow Graph x KnownFor (your interests are computed from who you follow)
- Post embeddings update dynamically each time someone favorites the post
- Cosine similarity >= 0.7 = relevance match
- Enforces topical fidelity -- off-topic content drift is demoted

### Shadow Hierarchy: Account Tiering

The algorithm quietly categorizes accounts into tiers:

**New Account Suppression ("Cold Start"):**

- Posts shown to only ~10% of normal initial distribution
- Example: Normal visibility = 1,000 impressions in 10 minutes; Cold start = 100 impressions in 10 minutes
- Content must earn extraordinary engagement from that tiny sample to break out
- This is why many new accounts "never take off" -- it is the algorithmic debt, not the content quality

**Engagement Debt:**

- Accounts accumulating poor engagement ratios get quietly suppressed
- Only consistent high-quality, interactive content reverses the debt
- Historical negative signals persist -- a bad week can reduce reach for months

### Phoenix Transformer Model (2026)

**Architecture:**

- Ported from Grok-1 open-source release, adapted for recommendation
- Two-stage: retrieval (two-tower) then ranking (transformer with candidate isolation)
- User tower: encodes engagement history into embeddings [B, S, D]
- Candidate tower: encodes post features into embeddings [B, C, D]
- Output: [B, num_candidates, num_actions] logits

**Key Innovation -- Candidate Isolation:**

- During inference, candidates cannot attend to each other
- Each candidate only attends to user context
- This ensures a post's score does not depend on what other posts are in the batch
- Makes scores consistent and cacheable across requests

**Design Principles:**

- No hand-engineered content relevance features
- The transformer learns relevance entirely from user engagement sequences
- Hash-based embeddings for efficient lookup across models
- Multi-action prediction (15+ engagement types simultaneously)

---

## 8. Tactical Implications

### Maximizing the Boost Window

**The first 30 minutes are everything:**

- Early engagement signals quality to the algorithm
- Tweets that gain traction quickly receive expanded distribution
- Tweets that sit dormant get permanently deprioritized
- Strategy: Post when your audience is most active; seed engagement quickly

**Premium subscribers get more forgiveness:**

- Their content gets distributed even if they miss peak windows by an hour or two
- 2-4x initial impression boost buys time for organic engagement to build

### Optimal Posting Strategy

**Frequency:**

- Minimum: 3 posts per day to maintain algorithmic relevance
- Optimal for reach: 15-30 posts daily (but ONLY if engagement per post stays high)
- Quality threshold: Better to post 10 high-quality tweets than 30 mediocre ones
- Wait 30-60 minutes between tweets to avoid self-cannibalization

**Timing:**

- Best overall: Wednesday at 9 AM
- Peak windows: 8 AM - 11 AM and 3 PM on weekdays
- Best days: Tuesday through Thursday
- Worst: Weekends (lower overall activity)

**Character Length:**

- Engagement sweet spot: 71-100 characters (concise, punchy)
- Like optimization: 240-259 characters (just under the standard limit)
- Threads: 3-5 tweets for maximum cumulative impressions
- Long-form (Premium only): Useful for dwell time signal, not directly boosted

### Content Strategies That Align With the Algorithm

**1. Prioritize Conversation Depth Over Broadcast Reach**

- Reply-engaged-by-author signal is worth 150x a like
- Always respond to replies on your tweets, especially early replies
- Ask genuine questions that invite substantive responses
- Write tweets that are "reply magnets" -- controversial takes, hot questions, fill-in-the-blank prompts

**2. Build Real Graph Score With Your Audience**

- Consistently engage with the same accounts (like, reply, retweet their content)
- This builds bidirectional Real Graph edges, making your content more likely to appear in their feed AND vice versa
- Comment on their tweets before posting your own -- primes the algorithm

**3. Use the Link Workaround**

- Never put links in the main tweet body
- Post your text content as the main tweet; add the link in a reply
- This avoids the 30-50% reach penalty
- For Premium accounts: links are less penalized but still suboptimal

**4. Media Strategy**

- Text-only posts actually outperform video by 30% on X (unique to this platform)
- When using video: 15-60 seconds, vertical (9:16), with captions, native upload only
- Images provide a secondary boost over plain text
- Never link to YouTube/external video -- upload natively

**5. Thread Strategy**

- 3-5 tweets per thread is optimal
- Front-load value in the first tweet (it gets the most distribution)
- Each subsequent tweet should add enough value to keep readers going
- Target 70-80% completion rate
- Threads get 40-60% more total impressions than equivalent standalone posts

**6. Hashtag Discipline**

- Maximum 1-2 niche, relevant hashtags
- 3+ hashtags triggers up to -40% penalty
- Niche hashtags outperform broad/trending ones for algorithmic matching

**7. Maintain Positive Sentiment**

- Grok's sentiment analysis rewards constructive, positive messaging
- Combative/negative tone reduces reach even with high engagement
- This does NOT mean you cannot be provocative -- just not hostile

**8. Protect Your TweepCred**

- Maintain a healthy follower-to-following ratio
- Avoid mass following/unfollowing
- Cultivate engagement from reputable accounts (their PageRank flows to you)
- Keep negative signals (blocks, mutes, reports) to an absolute minimum
- One week of poor behavior can reduce reach for months

**9. Premium Is Essentially Required for Serious Distribution**

- 10x more reach per post vs. free accounts
- 4x in-network and 2x out-of-network visibility boost
- Priority placement in replies, search, and timelines
- Link posts actually function (vs. zero engagement for free accounts)
- TweepCred bonus of +4 to +16 points

**10. For New Accounts: Break the Cold Start**

- Accept the 90% distribution penalty as reality
- Focus on producing content so good it gets extraordinary engagement from the small sample
- Engage heavily with established accounts to build Real Graph edges
- Subscribe to Premium immediately to offset cold start suppression
- Consistency matters more than volume in the early days

---

## 9. Sources

### Primary Technical Sources (GitHub)

- [twitter/the-algorithm](https://github.com/twitter/the-algorithm) -- Original open-source recommendation algorithm (2023)
- [twitter/the-algorithm-ml](https://github.com/twitter/the-algorithm-ml) -- ML model code including Heavy Ranker
- [Heavy Ranker README with exact weights](https://github.com/twitter/the-algorithm-ml/blob/main/projects/home/recap/README.md) -- Engagement probability weights configuration
- [Heavy Ranker weight update commit](https://github.com/twitter/the-algorithm-ml/commit/b85210863f7a94efded0ef5c5ccf4ff42767876c) -- Weighted engagement probability explanation
- [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) -- Grok-powered algorithm (January 2026)
- [Phoenix README](https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md) -- Grok transformer ranking model details
- [SimClusters README](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/simclusters_v2/README.md) -- Topic/interest matching system
- [TweepCred README](https://github.com/twitter/the-algorithm/blob/main/src/scala/com/twitter/graph/batch/job/tweepcred/README) -- Account reputation scoring
- [Awesome Twitter Algo annotations](https://github.com/igorbrigadir/awesome-twitter-algo) -- Community-annotated algorithm analysis

### Official X/Twitter Sources

- [Twitter's Recommendation Algorithm (X Engineering Blog)](https://blog.x.com/engineering/en_us/topics/open-source/2023/twitter-recommendation-algorithm) -- Official technical overview
- [Elon Musk on Grok integration](https://x.com/elonmusk/status/1979217645854511402) -- Announcement of Grok replacing legacy system

### Analysis & Research

- [X Shares Insights Into Key Ranking Factors (Social Media Today)](https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/)
- [X's Algorithm Shifting to Grok-Powered Model (Social Media Today)](https://www.socialmediatoday.com/news/x-formerly-twitter-switching-to-fully-ai-powered-grok-algorithm/803174/)
- [X Algorithmically Ranks Following Feed (Social Media Today)](https://www.socialmediatoday.com/news/x-formerly-twitter-sorts-following-feed-algorithm-ai-grok/806617/)
- [How the X Algorithm Works in 2026 (PostEverywhere)](https://posteverywhere.ai/blog/how-the-x-twitter-algorithm-works) -- 6 ranking factors breakdown
- [Major Twitter Algorithm Changes in 2025 (HashMeta)](https://hashmeta.com/insights/twitter-algorithm-changes-2025) -- Engagement weights and penalty details
- [Complete Technical Breakdown 2026 (TweetArchivist)](https://www.tweetarchivist.com/how-twitter-algorithm-works-2025)
- [Twitter Algorithm Explained 2026 (TweetArchivist)](https://www.tweetarchivist.com/twitter-algorithm-explained-2025)
- [Does X Premium Really Boost Your Reach? (Buffer)](https://buffer.com/resources/x-premium-review/) -- Analysis of 18M+ posts
- [Hidden X Algorithm: TweepCred, Shadow Hierarchy, Dwell Time (Circleboom)](https://blog-content.circleboom.com/the-hidden-x-algorithm-tweepcred-shadow-hierarchy-dwell-time-and-the-real-rules-of-visibility/)
- [Best Time to Post on X 2026 -- 700K Posts Analyzed (PostEverywhere)](https://posteverywhere.ai/blog/best-time-to-schedule-x-posts)
- [How Often to Post on Twitter 2026 (TweetArchivist)](https://www.tweetarchivist.com/how-often-to-post-on-twitter-2025)
- [X Algorithm Update January 2026 (Typefully)](https://typefully.com/blog/x-algorithm-open-source)
- [X Open-Sources Algorithm Powered by Grok AI (EONMSK News)](https://www.eonmsk.com/2026/01/20/x-open-sources-algorithm-powered-by-grok-ai/)
- [Deep Dive Inside X's Recommendation Algorithm (Medium/Gowtham Boyina)](https://thegowtham.medium.com/deep-dive-inside-x-fka-twitter-s-recommendation-algorithm-460b2bd4e26a)
- [Understanding the X Algorithm 2026 (SocialBee)](https://socialbee.com/blog/twitter-algorithm/)
- [How the X Algorithm Works 2025 (Sprout Social)](https://sproutsocial.com/insights/twitter-algorithm/)
- [TweepCred Deep Dive (Mark Morphew)](https://www.markmorphew.com/what-is-tweepcred-on-x/)
- [Unveiling TweepCred (BuildingThingsWithJavascript)](https://buildingthingswithjavascript.com/articles/unveiling-tweepcred-the-power-behind-twitters-recommendation-engine)

---

## Appendix: Quick Reference Card

### The Formula That Matters Most

```
Tweet Score =
  (P(reply_engaged_by_author) x 75.0)
+ (P(reply) x 13.5)
+ (P(good_profile_click) x 12.0)
+ (P(good_click) x 11.0)
+ (P(good_click_v2) x 10.0)
+ (P(retweet) x 1.0)
+ (P(fav) x 0.5)
+ (P(video_playback50) x 0.005)
- (P(negative_feedback) x 74.0)
- (P(report) x 369.0)
```

### The 5 Things That Matter Most (In Order)

1. **Reply to your repliers** (150x value of a like)
2. **Get replies** (27x value of a like)
3. **Avoid negative signals** (blocks/mutes = -74x; reports = -369x)
4. **Generate profile clicks and dwell time** (20-24x value of a like)
5. **Get bookmarks and retweets** (2-20x value of a like)

### What NOT to Do

1. Put links in the main tweet body (-30-50% reach; zero engagement if free account)
2. Use 3+ hashtags (-40% penalty)
3. Write in combative/negative tone (Grok sentiment filter)
4. Post high volume with low engagement (engagement debt)
5. Mass follow/unfollow (3-month shadowban risk)
6. Write in all caps (penalized)
7. Ignore replies to your tweets (you are leaving 150x signal value on the table)
