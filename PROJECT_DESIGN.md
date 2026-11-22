# Personal Expense Tracker

## 1. Project Overview

**Project Name:** Personal Expense Tracker

**Language:** Python

**Application Type:** Command-Line Application (CLI)

**Difficulty Level:** Intermediate

### Objective

The objective of this project is to develop a Python-based Personal Expense Tracker that allows users to record and manage their income and expenses.

The application helps users monitor spending habits, calculate their remaining balance, manage monthly budgets, and generate financial reports.

### Main Goals

- Record income and expenses.
- View, search, update, and delete transactions.
- Organize expenses into categories.
- Calculate total income, expenses, and remaining balance.
- Generate monthly financial reports.
- Generate category-wise expense reports.
- Set and monitor monthly budgets.
- Export transaction records to CSV.
- Store transaction and budget data using JSON.
- Maintain application logs.

## 2. Transaction Data Design

| Field Name | Data Type | Description |
|---|---|---|
| Transaction ID | Integer | Unique identification number |
| Transaction Type | String | Income or Expense |
| Amount | Integer / Float | Amount of money |
| Category | String | Transaction category |
| Description | String | Details of the transaction |
| Date | String | Transaction date (DD-MM-YYYY) |

## 3. Default Expense Categories

- Food
- Transportation
- Education
- Shopping
- Entertainment
- Bills
- Healthcare
- Other

Users can also enter their own categories.

## 4. Main Menu Design

The application provides a command-line menu through which users can access all application features.

### Application Menu

```text
========== PERSONAL EXPENSE TRACKER ==========

1. Add Transaction
2. View All Transactions
3. Update Transaction
4. Delete Transaction
5. Search Transaction
6. Financial Summary
7. Monthly Report
8. Category-wise Expenses
9. Set Monthly Budget
10. Check Monthly Budget
11. View Monthly Budget
12. Export Transactions to CSV
13. Exit

Enter your choice:
```

## 5. Input Validation and Error Handling

The application validates user inputs to prevent incorrect data from being stored and to avoid unexpected application crashes.

### Validation Rules

| Situation | Application Behaviour |
|---|---|
| User enters a negative or zero amount | Reject the amount |
| User enters an invalid date | Display an error message |
| User searches for a nonexistent transaction ID | Display transaction not found |
| User enters an invalid menu choice | Display an invalid choice message |
| User enters an invalid transaction type | Reject the transaction |
| User enters an empty category | Reject the input |
| User enters an empty description | Reject the input |
| JSON file contains invalid data | Reject invalid transaction data |

### Error Handling Approach

- Validate inputs before saving transactions.
- Display meaningful error messages.
- Handle invalid user input.
- Handle missing or corrupted JSON files.
- Use exception handling wherever necessary.
- Restore original transaction data if saving an update or deletion fails.

## 6. Financial Calculation Logic

The application automatically calculates financial summaries using recorded transactions.

### 1. Total Income

Total Income = Sum of all Income transactions.

### 2. Total Expenses

Total Expenses = Sum of all Expense transactions.

### 3. Remaining Balance

Remaining Balance = Total Income - Total Expenses.

### 4. Monthly Financial Report

The application filters transactions according to the selected month and year and calculates:

- Total monthly income.
- Total monthly expenses.
- Monthly balance.

### 5. Category-wise Expenses

The application groups expense transactions according to their categories and calculates the total spending for each category.

Example:

- Food = ₹1,100
- Transportation = ₹500
- Education = ₹700
- Shopping = ₹600

### 6. Monthly Budget Management

Users can set a budget for a particular month.

The application calculates:

- Monthly budget.
- Monthly expenses.
- Remaining budget.
- Percentage of budget used.

It also displays a warning when 80% or more of the budget is used and an alert when the budget is exceeded.

## 7. Technical Architecture

### 1. Project Structure

```text
Personal_Expense_Tracker/
│
├── main.py
├── models.py
├── manager.py
├── storage.py
├── reports.py
├── budget.py
├── exporter.py
├── logger.py
│
├── data/
│   ├── transactions.json
│   └── budgets.json
│
├── exports/
│   └── transactions.csv
│
├── logs/
│   └── app.log
│
├── PROJECT_DESIGN.md
├── README.md
├── requirements.txt
└── .gitignore
```

### 2. Module Responsibilities

| Component | Responsibility |
|---|---|
| main.py | Application entry point, menu and user interaction |
| models.py | Defines the Transaction class |
| manager.py | Handles adding, updating, deleting and searching transactions |
| storage.py | Handles JSON reading, writing and data validation |
| reports.py | Calculates financial summaries and monthly reports |
| budget.py | Manages monthly budgets and budget calculations |
| exporter.py | Exports transactions to CSV |
| logger.py | Configures application logging |

### 3. Supporting Directories

- **data/** - Stores transaction and budget JSON files.
- **exports/** - Stores exported CSV files.
- **logs/** - Stores application log files.

### 4. Architectural Principle

The application follows a modular architecture with a clear separation between:

1. User interaction.
2. Business logic.
3. Data storage.
4. Financial reporting.
5. Data export.
6. Application logging.

Each module has a specific responsibility, making the application easier to understand, maintain and extend.

## 8. Data Storage Design

The application uses JSON files for persistent data storage.

- `transactions.json` stores transaction records.
- `budgets.json` stores monthly budget information.

CSV export is used to create an external copy of transaction records.

## 9. Logging

The application uses Python's built-in logging module.

Application events and important operations are recorded in:

`logs/app.log`

Logging helps track transaction operations and identify saving errors.

## 10. Future Improvements

- Graphical User Interface (GUI).
- Database integration using SQLite.
- Data visualization using charts.
- Advanced financial analytics.
- User authentication.
- Cloud data synchronization.