import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from colorama import init, Fore
init(autoreset=True)

# Reference: Python Tutorial 7 - Formatting Output in Python
# Link: https://www.youtube.com/watch?v=Ln5dzg820PU
# This video helped me to make sure I formatted the programme in a structured way

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
    print(f"\nEnter your {data_type} data below:")

    date_input = input(Fore.MAGENTA + "Date (DD/MM/YYYY): ")
    category_input = input(Fore.MAGENTA + "Category: ")
    amount_input = input(Fore.MAGENTA + "Amount: ")
    description_input = input(Fore.MAGENTA + "Description (optional): ")

    data_list = [date_input.strip(), category_input.strip(),
                 amount_input.strip(), description_input.strip()]


    # Reference: Python Tutorial: Using Try/Except Blocks for Error Handling
    # Link: https://www.youtube.com/watch?v=NIWwJbo-9_8
    # This video showed me how to prompt users to input correct valid inputs when incorrect inputs were used


    while not validate_financial_data(data_list):
        print(
            "Invalid input, please re-enter your data"
            " following the correct format.")
        date_input = input(Fore.MAGENTA + "Date (DD/MM/YYYY): ")
        category_input = input(Fore.MAGENTA + "Category: ")
        amount_input = input(Fore.MAGENTA + "Amount: ")
        description_input = input(Fore.MAGENTA + "Description (optional): ")
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
                Fore.RED + "Missing required fields."
                " Please ensure all fields are entered correctly.")

        datetime.strptime(data[0], "%d/%m/%Y")
        # Reference: Advanced Exception Handling in Python
        # Link: https://www.youtube.com/watch?v=ZUqGMDppEDs
        # I was able to learn how to add a solid cheques for inputs the user made
        float(data[2])

    except ValueError as e:
        print(Fore.RED + f"Validation error: {e}")
        return False

    return True


def update_worksheet(data, worksheet_name):
    """
    add data to worksheet
    """
    try:
        print(Fore.BLUE + f"Updating {worksheet_name} worksheet...")
        worksheet = SHEET.worksheet(worksheet_name)
        worksheet.append_row(data)
        print(Fore.GREEN + f" {worksheet_name} worksheet updated")
    except Exception as e:
        print(Fore.RED + f"{e} update Failed")
        # Reference: Python Tutorial: Using Try/Except Blocks for Error Handling
        # Link: https://www.youtube.com/watch?v=NIWwJbo-9_8
        # Help me add error messages that would tell the user what went wrong and how to fix it / use a valid input



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

        print(Fore.BLUE + "\nFinancial Report\n")
        print(Fore.BLUE + f"Total Income: {total_income:.2f}")
        print(Fore.BLUE + f"Total Expenses: {total_expenses:.2f}")
        print(Fore.BLUE + f"Net Savings: {net_savings:.2f}")

    except Exception as e:
        print(Fore.RED + f"Report failed to generate: {e}")


def display_recent_entries(worksheet_name, num_entries=5):
    """
    display 5 recent entries from the specified worksheet.
    """

    try:
        worksheet = SHEET.worksheet(worksheet_name)
        entries = worksheet.get_all_values()[1:][::-1]
        recent_entries = entries[:5]

        print(f"\nMost Recent {worksheet_name} Entries:\n")
        print(
            f"{Fore.BLUE + 'Date':<17} {Fore.BLUE + 'Category':<26}"
            f"{Fore.BLUE + 'Amount':<15} {Fore.BLUE + 'Description'}")

        for entry in recent_entries:
            date, category, amount, description = entry
            print(f"{date:<12} {category:<20} {amount:<10} {description}")
        # Reference: Advanced Exception Handling in Python
        # Link: https://www.youtube.com/watch?v=ZUqGMDppEDs
        # Helped to understand the way in which I can tell the user that there is a problem in retrieving information from Google sheets
    except Exception as worksheet_name:
        print(
            Fore.RED + f"Failed to retrieve data from {worksheet_name}"
            " worksheet:")


def main():
    """
    main function to run the Budget Tracker options for both income"
    " and expenses and more
    """
    while True:
        action = input(
            "\nAre you adding data or do you what to display a total report or"
            "view the most recent entries \n"
            "To upload income data enter 'Income' \n"
            "To upload expenses data enter 'Expense'\n"
            "To view overall report enter 'Report'\n"
            "To view recent entries enter 'Recent'\n"
            "If not enter 'quit' to exit\n"
            "\nEnter here:").lower()
        if action in ["income", "expense"]:
            financial_data = get_financial_data(action)
            worksheet_name = "Income" if action == "income" else "Expenses"
            update_worksheet(financial_data, worksheet_name)
        elif action == "recent":
            entry_type = input(
                "\nWhich entries do you want to see? Enter 'income' or"
                " 'expenses':").lower()
            if entry_type == "income":
                display_recent_entries("Income")
            elif entry_type == "expenses":
                display_recent_entries("Expenses")
            else:
                display_recent_entries(entry_type)
        elif action == "report":
            generate_financial_report()
        elif action == "quit":
            print(Fore.CYAN + "Go make some money")
            break
        else:
            print(Fore.RED + "invalid option try again")


if __name__ == "__main__":
    # Reference: Python 101 Python Basics for Beginners Playlist
    # Link: https://www.youtube.com/watch?v=JTFGllcJ29I&list=PLNnG2akFozlISSPF2UiUFSHieGCc_BA9b
    # This video help me to understand Python better when using main() 
    print(Fore.WHITE + "\n   Welcome to the Budget Tracker")
    print(Fore.WHITE + "\nThe Budget Tracker will assist users in "
          "managing their finances by allowing them to record and monitor"
          " their income and expenses over time. This tool aims to"
          " provide clear visibility into financial habits, enabling"
          " better budgeting decisions.")

    main()
