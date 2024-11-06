# Budget Tracker Application

## Description
The Budget Tracker application helps users track income and expenses effectively using a user-friendly interface and Google Sheets for data storage. This application empowers users to make informed decisions about their spending and saving habits by simplifying the recording and analysis of financial transactions.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Future Enhancements](#future-enhancements)

## Installation
1. the repository template:
   
2. Navigate to the project directory:
  
3. Install the required packages:
   pip install gspread google-auth colorama
   
5. Set up the Google Sheets API and create your `creds.json` file. Follow the steps below for API setup.

### Google Sheets API Setup
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project.
3. Enable the Google Sheets API and the Google Drive API.
4. Create credentials:
   - Select "Service account" and follow the prompts.
   - Download the file, place it in your project directory, and rename it `creds.json`.
5. Share your Google Sheet with the service account email.

## Features
- **User-Friendly Interface**: Simple command-line interface for easy interaction and navigation.

- **Data Entry for Income and Expenses**: Allows users to input details for both income and expenses, including:
Date, category, amount, and optional description.

- **Input Validation**: Ensures accurate and correct data entry with checks for format and numbers.

- **Google Sheets Integration**: Utilizes Google Sheets for real-time data storage and retrieval.Automatically updates the appropriate worksheet (Income or Expenses) upon data entry.

- **Financial Reporting**: Generates a summary report of total income, total expenses, and net savings. Provides clear insights into financial. [Screen shot]

- **Recent Entries Display**: Displays the five most recent entries from either the Income or Expenses worksheet. Allows users to quickly review their latest financial activities. [Screen shot]

- **Error Handling**: Catches exceptions during data retrieval and updates, providing informative error messages to users. [Screen shot]

- **Customizable Entry Categories**: Users can input custom categories for income and expenses, enhancing tracking flexibility. [Screen shot]

- **Quit Functionality**: Provides an option to exit the application gracefully. [Screen shot]

- **Color-Coded Output**: Utilizes the colorama library for color-coded text in the terminal, improving readability and user experience. [Screen shot]


## Usage
### Adding Income or Expense Data
- When prompted, enter the type of financial data you want to add (either "Income" or "Expense").
- Follow the input prompts:
  - **Date (DD/MM/YYYY)**: Enter the date of the transaction.
  - **Category**: Specify the category of the income or expense (e.g., Salary, Groceries).
  - **Amount**: Enter the amount, ensuring it's a positive number.
  - **Description (optional)**: Provide additional details about the transaction.

### Generating Financial Reports
- Enter "Report" when prompted to view your financial summary, including total income, total expenses, and net savings.

### Displaying Recent Entries
- Enter "Recent" and specify whether you want to see "income" or "expenses" entries. The application will display the five most recent entries from the specified worksheet.

## Configuration
- Ensure the Google Sheets URL is correctly specified in your application code if applicable.

## Troubleshooting
- **Common Issues**:
  - If you encounter issues, ensure your `creds.json` file is in the correct directory and contains valid credentials.
  - Check for internet connectivity when accessing Google Sheets.
  - Review the input validation messages for guidance on correcting any data entry errors.

## Contributing
- Contributions are welcome! Feel free to submit issues or pull requests for enhancements, and include a description of your changes.

## Contact
For questions or feedback, please reach out to me at [your-email@example.com] or visit my [GitHub profile](https://github.com/your-username).

## Acknowledgments
- Special thanks to the developers of gspread and colorama for their fantastic libraries that enabled the functionality of this application.

## Future Enhancements
1. Create a report function that allows users to display financial data for specific dates or months.
2. Improve the recent entries feature to prioritize the most recent date rather than the most recent entry.
3. Implement a multiple-choice category selection for income or expense entries to enhance data filtering in Google Sheets.
