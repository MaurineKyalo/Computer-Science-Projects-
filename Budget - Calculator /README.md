# 🐍 Budget Calculator Algorithm

## Project Overview
This is a Python-based command-line application that calculates a user's monthly budget. It takes user input for income and expenses, processes the data, and provides a summary of the remaining budget.

## 🧠 The Logic and Algorithm
This project demonstrates foundational programming concepts, specifically **sequencing**, **conditional selection**, and **iterative loops**. Here is how the logic flows:

1. **Input (Sequencing):** The program first prompts the user to input their total monthly income and their fixed expenses (e.g., rent, utilities).
2. **Iterative Loop:** It then enters a `while` loop that allows the user to add multiple variable expenses (e.g., groceries, entertainment) one by one. The loop continues until the user types 'no'.
3. **Calculation:** The program calculates the total expenses (fixed + variable) and subtracts that from the income to find the remaining budget.
4. **Conditional Selection:** Finally, it uses `if/elif/else` statements to evaluate the remaining budget:
   - If it's greater than 0, it tells the user they have a surplus.
   - If it's less than 0, it warns them they are over budget.
   - If it's exactly 0, it tells them the budget is balanced.

## 🛠️ How to Run
To run this script locally, you need Python 3 installed. 
1. Open your terminal.
2. Navigate to this folder.
3. Run: `python budget_calculator.py`