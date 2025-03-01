# Expense Tracker Application

This is a simple expense tracker application that allows users to manage their expenses efficiently. Users can add, update, delete, and view their expenses, as well as receive summaries of all expenses and monthly expenses for the current year.

## Features

- Add new expenses with descriptions and amounts.
- Update existing expenses.
- Delete expenses.
- View all expenses.
- Get summaries of total expenses and monthly breakdowns.

## Project Structure

```
expense-tracker
├── src
│   ├── __init__.py
│   ├── expense_tracker.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── expense_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   └── expense.py
│   ├── views
│   │   ├── __init__.py
│   │   └── expense_view.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd expense-tracker
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/expense_tracker.py
```

Follow the on-screen prompts to manage your expenses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.