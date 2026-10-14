# 🐍 CodeAlpha Python Programming Internship Tasks

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![CodeAlpha](https://img.shields.io/badge/Internship-CodeAlpha-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

This repository contains all 4 completed tasks for the **CodeAlpha Python Programming Internship**. These projects cover core Python concepts, data structures, file I/O, regular expressions, web requests, and rule-based logic.

---

## 📂 Projects Overview

| Task # | Project Name | Key Concepts Used | Script File |
| :--- | :--- | :--- | :--- |
| **Task 1** | [Hangman Game](#-task-1-hangman-game) | `random`, `while loop`, `if-else`, `strings`, `lists`, `sets` | `hangman.py` |
| **Task 2** | [Stock Portfolio Tracker](#-task-2-stock-portfolio-tracker) | `dictionary`, `input/output`, `basic arithmetic`, `file handling (CSV)` | `portfolio_tracker.py` |
| **Task 3** | [Task Automation Scripts](#-task-3-task-automation-with-python-scripts) | `os`, `shutil`, `re`, `requests`, `file handling` | `task_automation.py` |
| **Task 4** | [Basic Chatbot](#-task-4-basic-chatbot) | `if-elif`, `functions`, `loops`, `input/output` | `chatbot.py` |

---

## 🎮 Task 1: Hangman Game

### 📌 Goal
Create a simple text-based Hangman game where the player guesses a word one letter at a time.

### ✨ Scope & Features
- Uses a predefined list of 5 words selected randomly via the `random` module.
- Limits incorrect guesses to a maximum of **6 attempts**.
- Tracks guessed letters using a `set` for instant lookup and duplicate prevention.
- Pure console input/output with input validation.

### 🚀 How to Run
```bash
python hangman.py
