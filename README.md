# 🐍 CodeAlpha Python Programming Internship Tasks

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CodeAlpha](https://img.shields.io/badge/Internship-CodeAlpha-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

This repository contains the completed tasks for the **CodeAlpha Python Programming Internship**. Each project demonstrates fundamental Python concepts including data structures, file handling, regular expressions, and task automation.

---

## 📂 Projects Overview

| Task # | Project Name | Key Concepts | File |
| :--- | :--- | :--- | :--- |
| **Task 1** | [Hangman Game](#-task-1-hangman-game) | `random`, `while loop`, `sets`, `strings`, `lists` | `hangman.py` |
| **Task 2** | [Stock Portfolio Tracker](#-task-2-stock-portfolio-tracker) | `dictionaries`, `input validation`, `csv file I/O` | `portfolio_tracker.py` |
| **Task 3** | [Task Automation Script](#-task-3-task-automation-with-python) | `os`, `shutil`, `re`, `requests`, `file handling` | `task_automation.py` |

---

## 🎮 Task 1: Hangman Game

### 📌 Goal
A text-based console Hangman game where the player guesses a hidden word one letter at a time within a limited number of attempts.

### ✨ Features
- Predefined pool of words selected randomly using the `random` module.
- Maximum of **6 incorrect guesses** allowed.
- Real-time tracking of guessed letters using a Python `set` to prevent duplicate entries.
- Input validation ensuring only single alphabetical characters are accepted.

### 🚀 How to Run
```bash
python hangman.py
