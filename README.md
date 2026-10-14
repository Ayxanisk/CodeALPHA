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
```
📈 Task 2: Stock Portfolio Tracker
📌 Goal
Build a simple stock tracker that calculates total investment value based on manually defined stock prices.

✨ Scope & Features
Hardcoded dictionary defining stock prices (e.g., {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 175, "MSFT": 420}).

Interactive prompt where the user inputs stock ticker names and quantities.

Calculates and displays a formatted table of individual holdings and total investment value.

Optional export of the portfolio summary to a .csv or .txt file.

🚀 How to Run

```Bash
python portfolio_tracker.py

```
⚙️ Task 3: Task Automation with Python Scripts
📌 Goal
Automate small, real-life repetitive tasks using Python modules.

✨ Implemented Automation Workflows (Choose/Include)
JPG File Mover (os, shutil): Scans a source directory and moves all .jpg image files into a newly created destination folder.

Email Address Extractor (re, file handling): Reads a .txt file, extracts all valid email addresses using Regular Expressions, and saves them into a separate output file.

Webpage Title Scraper (requests, re, file handling): Sends an HTTP request to a fixed webpage URL, scrapes the <title> tag, and saves it locally.

🚀 How to Run

```Bash
python task_automation.py

```

🤖 Task 4: Basic Chatbot
📌 Goal
Build a simple rule-based console chatbot capable of holding a basic conversation.

✨ Scope & Features
Processes user inputs such as "hello", "how are you", "what is your name", and "bye".

Responds with predefined replies ("Hi!", "I'm fine, thanks!", "Goodbye!").

Structured with modular functions, a continuous while conversation loop, and normalized string matching (if-elif-else).

🚀 How to Run

```Bash
python chatbot.py

```
