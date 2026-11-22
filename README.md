# Personal Expense Tracker

A Python-based command-line application to manage personal income, expenses, budgets, and financial reports.

## Features

- Add, view, search, update, and delete transactions.
- Track income and expenses.
- Calculate total income, expenses, and current balance.
- Generate monthly financial reports.
- View category-wise expenses.
- Set and monitor monthly budgets.
- Export transactions to CSV.
- Store transaction and budget data using JSON.
- Validate user inputs and stored data.
- Handle errors and maintain application logs.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- CSV
- Exception Handling
- Logging
- File Handling

## Project Structure

```text
Personal_Expense_Tracker/
│
├── main.py
├── models.py
├── manager.py
├── storage.py
├── reports.py
├── budget.py
├── exceptions.py
├── exporter.py
├── logger.py
│
├── data/
├── exports/
├── logs/
│
├── tests/
├── PROJECT_DESIGN.md
├── README.md
└── requirements.txt
```

## How to Run

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

```bash
py main.py
```

## Data Storage

- Transactions are stored in `data/transactions.json`.
- Monthly budgets are stored in `data/budgets.json`.
- CSV exports are saved in `exports/transactions.csv`.
- Application logs are saved in `logs/app.log`.

## Date Formats

- Transaction date: `DD-MM-YYYY`
- Budget month: `MM-YYYY`

## Future Improvements

- Graphical user interface (GUI).
- Database integration using SQLite.
- Data visualization.
- Advanced financial analytics.

## Author

Developed as a Python project to practice backend development, OOP, file handling, data validation, and software design.