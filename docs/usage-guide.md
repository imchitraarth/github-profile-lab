# Usage Guide

Welcome to github-profile-lab! This guide covers everything in this repo.

## Tools

### badge_generator.py

Generates shields.io badge markdown for GitHub READMEs.

`ash
python tools/badge_generator.py --label build --message passing --color brightgreen
`ash

## GitHub Actions

The markdown-lint workflow runs on every push to main that changes .md files.

`ash
npm install -g markdownlint-cli
markdownlint '**/*.md' --ignore node_modules
`ash

## Issue Templates

- Bug Report: for reporting bugs
- Feature Request: for suggesting improvements

## Contributing

See CONTRIBUTING.md for guidelines.
