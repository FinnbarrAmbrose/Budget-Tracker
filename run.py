import gspread
from google.oauth2.service_account import Credentials 
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Budget Tracker")

def get_financial_data(data_type):
    """
    users income,expenses  data
    """
    example = "Example: 01/10/2024, Salary, 3000, Monthly base salary" if data_type == "Example: income" else "01/10/2024, Rent, 1200, Monthly rent payment"
    print(f"enter {data_type} data in the format: Date, Category, Amount, Description (optional).")
    print(f"{example}")


    while True:
        data_str = input(f"Enter {data_type} here:\n")
        data_list = [entry.strip() for entry in data_str.split(',')]

        if validate_financial_data(data_list):
            print(f"{data_type.capitalize()} data is valid!")
            break
        else:
            print("Invalid input, please follow the format in Example ")
        



    return data_list
    



def validate_financial_data(data):
    """
    Validate uesr financial data
    """
    try:
        if len(data) < 3:
            raise ValueError("Incomplete data, please follow the format in Example ")

        datetime.strptime(data[0], "%d/%m/%Y")
        float(data[2])
        
    except ValueError as e:
        print(f"{e} Error")
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

def generate_financial_report();
""" 
Generate a financial report from Income and Expenses worksheets.
"""


 print("\nFinancial Report")
        print(f"Total Income")
        print(f"Total Expenses")
        print(f"Net Savings ")

except Exception as e:
        print(f"Report failed to generate")


def main ():
    """
    main function to run the Budget Tracker options for both income and expenses
    """
    while True:
        action = input("Are you adding income or expense data? Enter 'income', 'expense' if not Enter 'quit' to exit: ").lower()
        if action in ["income", "expense"]:
            financial_data = get_financial_data(action)
            worksheet_name = "income" if action == "income" else "Expenses"
            update_worksheet(financial_data, worksheet_name)
        elif action == "quit":
            print("go make some money before you try agein")
            break
        else:
            print("invalid option try again")

if __name__ == "__main__":
    print("Welcome to the Budget Tracker")
    main()