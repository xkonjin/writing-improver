VENV := .venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python
PYTEST := $(BIN)/pytest
RUFF := $(BIN)/ruff

.PHONY: install test lint check scan clean

install: $(VENV)/pyvenv.cfg

$(VENV)/pyvenv.cfg:
	python3 -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"

test: install
	$(PYTEST) tests/ -v

lint: install
	$(RUFF) check src/ tests/

check: lint test

scan: install
	@if [ -z "$(FILE)" ]; then echo "Usage: make scan FILE=path/to/article.md"; exit 1; fi
	$(PYTHON) -m src.cli scan $(FILE)

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache .mypy_cache src/__pycache__ **/__pycache__
