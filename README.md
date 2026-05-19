# Billing Management System

## Description
A Python-based terminal application designed to process and manage weekly employee billing data. It collects hours worked, calculates standard and overtime pay, stores the invoice records, and provides ad-hoc monthly billing reports with aggregates. 

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the source code.
3. Navigate to the project directory:
   ```bash
   cd billing-system
   ```

## Usage
Run the main menu application using Python:
```bash
python src/main.py
```

You will be presented with a menu of options:
- **0 - End**: Exit the application.
- **1 - Enter billing data**: Prompts for employee details (name, rate, weeks worked) to calculate standard/overtime pay and updates the billing data file.
- **2 - Display ad-hoc billing report**: Reads existing billing data and summarizes billable hours and amounts due across all employees.

## Project Structure
```
billing-system/
├── src/
│   ├── __init__.py
│   ├── main.py         # Application entry point and menu
│   ├── utils.py        # Shared billing utilities (formerly BillingModule.py)
│   ├── data_entry.py   # Data entry and calculations (formerly program4.py)
│   └── report.py       # Report generation logic (formerly program5.py)
├── data/               # Persistent data storage (e.g., Billing.txt)
├── tests/              # Test suite (to be implemented)
└── README.md
```
