# is218_test - Assignment 1: GitHub Issue-Driven Development

A professional Python project demonstrating best practices in issue-driven development and test-driven design.

## 📋 Project Overview

This project showcases how to connect GitHub issues to commits and build professional software using:
- Clear issue descriptions that tell a project story
- Detailed commits referenced to specific issues
- Comprehensive test coverage
- Reproducible development environments
- Professional documentation

**Status**: ✅ Complete - All issues closed with verification

## ⚙️ Python Environment Setup

**Python Version**: 3.9.6

**Create Virtual Environment**:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**Reactivate in New Terminal Sessions**:
```bash
source .venv/bin/activate
```

## 📁 Project Structure

| File | Purpose |
|------|---------|
| **README.md** | Project documentation and setup instructions (this file) |
| **.gitignore** | Excludes .venv/, __pycache__/, *.pyc, and .pytest_cache/ |
| **requirements.txt** | Python dependencies (pytest==8.4.2) |
| **app.py** | Core module with add() function |
| **tests/test_app.py** | Comprehensive test suite (3 test cases) |

## 🧪 Running Tests

With the virtual environment activated:
```bash
python -m pytest -v
```

Expected output:
```
tests/test_app.py::test_add_basic PASSED                               [ 33%]
tests/test_app.py::test_add_with_zero PASSED                           [ 66%]
tests/test_app.py::test_add_negative_numbers PASSED                    [100%]

============================== 3 passed in 0.00s ===============================
```

## 📚 What Gets Ignored

Git automatically excludes these files/folders to keep the repository clean:

- **.venv/** - Virtual environment (large, system-specific, regenerates)
- **__pycache__/** - Python bytecode cache (auto-generated)
- **\*.pyc, \*.pyo, \*.pyd** - Compiled Python files (auto-generated)
- **.pytest_cache/** - Test framework cache (temporary)

## 📖 Related Documentation

Start with terminal basics, connect your computer to GitHub, then practice everyday Git workflows:

1. [Basic file operations and navigation on Linux and macOS](docs/linux-macos-basics.md) — Paths, directories, copying, moving, deleting, reading, and finding files, with a practice exercise.
2. [Set up SSH keys and GitHub on Linux and macOS](docs/ssh-github-setup.md) — Configure Git, create an SSH key, connect it to GitHub, and clone or push a repository.
3. [Basic Git commands with real-life examples](docs/git-basics.md) — Start projects, collaborate, undo mistakes, manage stashes, and use staging and commit shortcuts such as `git add -p` and `git commit -am`.
