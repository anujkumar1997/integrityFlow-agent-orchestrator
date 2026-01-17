.PHONY: help venv install run test clean clean-all

help:
	@echo "Available commands:"
	@echo "  make venv        - Create virtual environment"
	@echo "  make install     - Install Python dependencies"
	@echo "  make run         - Run the app"
	@echo "  make test        - Run tests"
	@echo "  make clean       - Remove cache files"
	@echo "  make clean-all   - Remove cache + virtual env"

venv:
	python3 -m venv .venv
	@echo "Virtual environment created"

install:
	. .venv/bin/activate && pip install -U pip
	. .venv/bin/activate && pip install pydantic requests pytest
	@echo "Dependencies installed"

run:
	. .venv/bin/activate && python -m src.app

test:
	. .venv/bin/activate && python -m pytest -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	@echo "Cache files removed"

clean-all: clean
	rm -rf .venv
	@echo "Cache + virtual environment removed"
