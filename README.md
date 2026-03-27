# Software Testing Project

**Course:** 241-152 BAISD

**Student ID:** 6810110354

**Name:** นายศุภกิตติ์ เชี่ยวหมอน (Supphakit Cheawmon)

---

## Overview

This repository contains a comprehensive software testing project demonstrating best practices in Python unit testing. The project implements various algorithmic problems from HackerRank and similar platforms, each with complete test suites achieving 100% code coverage using Python's `unittest` framework.

## Project Structure

```
software-testing/
├── problems/
│   ├── cat_mouse/
│   │   ├── cat_mouse.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_cat_mouse.py
│   │   └── README.md
│   ├── alternating_characters/
│   │   ├── alternating_characters.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_alternating_characters.py
│   │   └── README.md
│   ├── caesar_cipher/
│   │   ├── caesar_cipher.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_caesar_cipher.py
│   │   └── README.md
│   ├── fizzbuzz/
│   │   ├── fizzbuzz.py
│   │   ├── tests/
│   │   │   └── test_fizzbuzz.py
│   │   └── README.md
│   ├── funny_string/
│   │   ├── funny_string.py
│   │   ├── tests/
│   │   │   └── test_funny_string.py
│   │   └── README.md
│   ├── grid_challenge/
│   │   ├── grid_challenge.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_grid_challenge.py
│   │   └── README.md
│   ├── number_utils/
│   │   ├── number_utils.py
│   │   ├── tests/
│   │   │   └── test_number_utils.py
│   │   └── README.md
│   ├── staircase/
│   │   ├── staircase.py
│   │   ├── tests/
│   │   │   └── test_staircase.py
│   │   └── README.md
│   └── two_characters/
│       ├── two_characters.py
│       ├── tests/
│       │   ├── __init__.py
│       │   │   └── test_two_characters.py
│       └── README.md
├── README.md
└── .git/
```

## Problems Implemented

1. **Cat and Mouse Game** - Determine which cat catches the mouse first
2. **Alternating Characters** - Find minimum deletions for alternating string
3. **Caesar Cipher** - Implement Caesar cipher encryption
4. **FizzBuzz** - Classic FizzBuzz problem
5. **Funny String** - Check if string is funny based on character differences
6. **Grid Challenge** - Sort grid rows and check column sorting
7. **Number Utils** - Utility functions for number operations
8. **Staircase** - Print staircase pattern
9. **Two Characters** - Find longest substring with two alternating characters

## Problems Summary

| Problem | Description | Lines of Code | Test Cases | Coverage |
|---------|-------------|---------------|------------|----------|
| Cat and Mouse | Determines which cat reaches the mouse first | 8 | 30 | 100% |
| Alternating Characters | Minimum deletions for alternating string | 14 | 27 | 100% |
| Caesar Cipher | Caesar cipher encryption | 8 | 42 | 100% |
| FizzBuzz | Classic FizzBuzz problem | 10 | 15 | 100% |
| Funny String | Check if string is funny | 50 | 20 | 100% |
| Grid Challenge | Sort grid rows and check column sorting | 9 | 27 | 100% |
| Number Utils | Utility functions for numbers | 10 | 20 | 100% |
| Staircase | Print staircase pattern | 8 | 12 | 100% |
| Two Characters | Longest substring with two alternating characters | 20 | 46 | 100% |

**Total Lines of Code:** 137

**Total Test Cases:** 239

**Overall Coverage:** 100%

## Testing Methodology

### Framework Used
- **unittest**: Python's built-in unit testing framework
- **coverage.py**: For code coverage analysis

### Testing Practices
- **100% Code Coverage**: All statements and branches tested
- **Edge Cases**: Boundary values, empty inputs, extreme cases
- **Comprehensive Test Cases**: Multiple scenarios per function
- **Descriptive Test Names**: Clear indication of what each test validates
- **Test Organization**: Logical grouping of related tests

### Coverage Goals
- Statement Coverage: 100%
- Branch Coverage: Complete decision path testing
- No uncovered lines in production code

## How to Run Tests

Each problem has its own test suite. To run tests for a specific problem:

```bash
cd problems/<problem_name>
python -m pytest tests/  # if pytest installed
# or
python -m unittest discover tests/
```

To run coverage analysis:

```bash
cd problems/<problem_name>
coverage run -m unittest discover tests/
coverage report
```

## Requirements

- Python 3.6+
- coverage package (optional, for coverage analysis)

Install requirements:
```bash
pip install coverage
```

## Academic Purpose

This project was developed as part of the Software Testing course (241-152 BAISD) to demonstrate practical application of testing principles in algorithm implementation.

---

**Note:** Detailed specifications, test coverage analysis, and implementation details for each problem are available in the respective code files and test suites.
