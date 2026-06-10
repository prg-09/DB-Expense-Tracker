# Expense Tracker CLI

A simple command-line Expense Tracker built with Python and SQLite that allows users to manage daily expenses efficiently. The application supports adding, viewing, editing, and deleting expenses while storing all data persistently in a local SQLite database.

## Features

- Add new expenses
- View all expenses
- Edit existing expenses
- Delete expenses
- Automatically records the current date
- Persistent data storage using SQLite
- Input validation for expense amounts and IDs
- User-friendly command-line interface

## Technologies Used

- Python 3
- SQLite3
- Datetime Module

## Project Structure

```text
expense-tracker/
│
├── main.py
├── expenses.db
└── README.md
```

## Database Schema

The application automatically creates the following table if it does not already exist:

```sql
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount INTEGER NOT NULL,
    description TEXT
);
```

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd expense-tracker
```

### Run the Program

```bash
python main.py
```

## Usage

When the application starts, the following menu is displayed:

```text
1. Add Expense
2. View Expenses
3. Edit Expense
4. Delete Expense
5. Exit
```

### Add Expense

The application automatically records the current date.

Users are prompted to enter:

- Expense category
- Expense amount
- Description

Example:

```text
Enter the category of your expense: Food
Enter the amount of your expense: 250
Enter a description for your expense: Lunch
```

Stored record:

```text
Date: 2026-06-10
Category: Food
Amount: 250
Description: Lunch
```

### View Expenses

Displays all expenses stored in the database.

Example:

```text
ID: 1
Date: 2026-06-10
Category: Food
Amount: Rs.250
Description: Lunch
```

### Edit Expense

Update an expense by entering its ID and providing new values.

The date is automatically updated to the current date when an expense is modified.

### Delete Expense

Delete an expense by entering its ID.

## Input Validation

The application validates:

- Expense IDs must be integers.
- Expense amounts must be numeric.
- Invalid entries prompt the user to re-enter the data.

## Skills Demonstrated

This project demonstrates:

- CRUD Operations (Create, Read, Update, Delete)
- SQLite Database Management
- SQL Queries
- Database Design
- Data Persistence
- Python Functions
- Exception Handling
- Input Validation
- Working with Dates using Python

## Challenges Faced

During development, several challenges were encountered:

- Learning how SQLite databases interact with Python.
- Understanding SQL operations such as INSERT, SELECT, UPDATE, and DELETE.
- Implementing input validation to prevent invalid user inputs.
- Handling database queries safely using parameterized SQL statements.
- Managing database records efficiently through CRUD operations.

## Future Improvements

Possible future enhancements include:

- Monthly expense summaries
- Category-wise spending reports
- Search expenses by category
- Filter expenses by date range
- Export expenses to CSV
- Data visualization using charts
- Budget tracking and spending limits
- Django web application version
- User authentication and multiple user accounts

## Learning Outcomes

Through this project, I learned:

- How relational databases work
- How to connect Python applications to SQLite databases
- How CRUD applications are implemented
- The importance of input validation
- Database schema design
- Writing cleaner and more maintainable code
- Using Python's datetime module for date management

## Author

Pragya Dhungel

Built as a learning project while exploring Python, SQL, and database-driven applications.