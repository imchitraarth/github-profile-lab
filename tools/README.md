# Tools

This directory contains small, useful CLI utilities for developers.

## badge_generator.py

Generate shields.io badge markdown for your GitHub README.

### Requirements
- Python 3.8+
- No external dependencies (uses standard library only)

### Usage

bash
python badge_generator.py --label build --message passing --color brightgreen


### Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| --label | Left badge text | required |
| --message | Right badge text | required |
| --color | Badge color name or hex | blue |
| --style | Badge style | flat |
| --list-colors | Show preset colors | - |

### Example Output

bash
![build: passing](https://img.shields.io/badge/build-passing-brightgreen?style=flat)

