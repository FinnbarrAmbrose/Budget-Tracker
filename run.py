import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Budget Tracker")


def get_financial_data(data_type):
    """
    Users income or expenses data.
    """
    print(f"Enter your {data_type} data below:")

    date_input = input("Date (DD/MM/YYYY): ")
    category_input = input("Category: ")
    amount_input = input("Amount: ")
    description_input = input("Description (optional): ")

    data_list = [date_input.strip(), category_input.strip(),
                 amount_input.strip(), description_input.strip()]

    while not validate_financial_data(data_list):
        print("Invalid input, please re-enter your data following the correct format.")
        date_input = input("Date (DD/MM/YYYY): ")
        category_input = input("Category: ")
        amount_input = input("Amount: ")
        description_input = input("Description (optional): ")
        data_list = [date_input.strip(), category_input.strip(),
                     amount_input.strip(), description_input.strip()]

    print(f"{data_type.capitalize()} data is valid!")
    return data_list


def validate_financial_data(data):
    """
    Validate user's financial data.
    """
    try:
        if len(data) < 3 or not data[0] or not data[1] or not data[2]:
            raise ValueError(
                "Missing required fields. Please ensure all fields are entered correctly.")

        datetime.strptime(data[0], "%d/%m/%Y")

        float(data[2])

    except ValueError as e:
        print(f"Validation error: {e}")
        return False

    return True


def update_worksheet(data, worksheet_name):
    """
    add data to worksheet
    """
    try:
        print(f"Updating {worksheet_name} worksheet...")
        worksheet = SHEET.worksheet(worksheet_name)
        worksheet.append_row(data)
        print(f" {worksheet_name} worksheet updated")
    except Exception as e:
        print(f"{e} update Failed")


def generate_financial_report():
    """ 
    Generate a financial report from Income and Expenses worksheets.
    """
    try:
        income_sheet = SHEET.worksheet("Income")
        expenses_sheet = SHEET.worksheet("Expenses")
        income_data = income_sheet.get_all_values()[1:]
        expenses_data = expenses_sheet.get_all_values()[1:]

        total_income = sum(float(row[2]) for row in income_data)
        total_expenses = sum(float(row[2]) for row in expenses_data)

        net_savings = total_income - total_expenses

        print("\nFinancial Report\n")
        print(f"Total Income{total_income:.2f}")
        print(f"Total Expenses{total_expenses:.2f}")
        print(f"Net Savings {net_savings:.2f}\n")

    except Exception as e:
        print(f"Report failed to generate")


def main():
    """
    main function to run the Budget Tracker options for both income and expenses
    """
    while True:
        action = input(
            "Are you adding income or expense data or do you what to generate Report? Enter 'income', 'expense', 'report' if not Enter 'quit' to exit: ").lower()
        if action in ["income", "expense"]:
            financial_data = get_financial_data(action)
            worksheet_name = "Income" if action == "income" else "Expenses"
            update_worksheet(financial_data, worksheet_name)
        elif action == "report":
            generate_financial_report()
        elif action == "quit":
            print("go make some money before you try agein")
            break
        else:
            print("invalid option try again")


if __name__ == "__main__":
    print("Welcome to the Budget Tracker")
    main()
