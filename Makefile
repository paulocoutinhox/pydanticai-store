.PHONY: help install run clean format

# Default target
help:
	@echo "Available commands:"
	@echo "  install  - Install dependencies"
	@echo "  run      - Run the chat application"
	@echo "  clean    - Clean cache and temporary files"
	@echo "  format   - Format code with black"

# Install dependencies
install:
	pip install -r requirements.txt

# Run the application
run:
	streamlit run main.py

# Clean cache and temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .coverage

# Format code with black
format:
	black .

# Setup development environment
dev-setup: install
	pip install black

# Create virtual environment
venv:
	python3 -m venv .venv
	@echo "Virtual environment created. Activate it with:"
	@echo "  source venv/bin/activate  # On macOS/Linux"
	@echo "  venv\\Scripts\\activate     # On Windows"
