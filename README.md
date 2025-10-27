# Inventory Management System - Static Analysis Lab

## Overview

This project demonstrates the use of static analysis tools to identify and fix code quality issues in a Python inventory management system. The lab focuses on improving code security, readability, and adherence to Python best practices.

## Project Files

- `inventory_system.py` - Main application with inventory management functions
- `reflection.md` - Analysis of the static analysis process and findings
- `pylint_report.txt` - Pylint analysis results
- `bandit_report.txt` - Security scan results
- `flake8_report.txt` - Style check results

## Running the Application

```bash
python inventory_system.py
```

## Code Quality Results

- **Pylint Score**: 10/10
- **Bandit Security Issues**: 0
- **Flake8 Style Violations**: 0

## Key Improvements

- Fixed security vulnerabilities (eval usage, bare exceptions)
- Resolved mutable default argument bug
- Added input validation and proper error handling
- Implemented proper file handling with context managers
- Added comprehensive documentation
- Applied PEP 8 style guidelines

## Running Static Analysis

```bash
pylint inventory_system.py > pylint_report.txt
bandit -r inventory_system.py > bandit_report.txt
flake8 inventory_system.py > flake8_report.txt
```
