# Playworld Arcade Suite

## Overview
Playworld is an interactive, console-based digital arcade system engineered to unify classic decision-making, probabilistic, and strategic mini-games under a single execution framework. It consolidates five mini-games into a single execution stream with a centralized menu.

## Features
* **Unified Console Menu:** Switch between 5 different mini-games seamlessly.
* **Input Resilience:** Cleans up accidental whitespaces and typing variations.
* **Defensive Error Handling:** Uses try-except blocks to catch text entry errors inside numeric games without crashing.
* **5 Classic Games:** Includes Rock-Paper-Scissors, Snake-Water-Gun, Roll a Dice, Card Higher/Lower, and Guess the Number.

## Technologies Used
* **Language:** Python 3.x
* **Core Libraries:** `random`, `sys`, `unittest`

## Steps to Install & Run
1. Ensure you have Python installed on your computer.
2. Download or clone this repository to your machine.
3. Open your Command Prompt (Windows) or Terminal (Mac/Linux).
4. Navigate to the project directory:
   ```bash
   cd path/to/playworld_project
   ```
5. Launch the application:
   ```bash
   python main.py
   ```

## Instructions for Testing
To execute automated verification checks, open your terminal inside the project directory and run:
```bash
python -m unittest discover tests
```
For manual testing, run the game and input unexpected choices (like letters instead of numbers) to verify that the error handling systems catch them successfully.
