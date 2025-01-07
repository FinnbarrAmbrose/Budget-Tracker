# Budget Tracker Application

## Description
The Budget Tracker application helps users track income and expenses effectively using a user-friendly interface and Google Sheets for data storage. This application empowers users to make informed decisions about their spending and saving habits by simplifying the recording and analysis of financial transactions. the Barefoot to using this programme is its features such as Real-time data integration with Google Sheets, customizable categories, and financial summaries.

###Target Audience 
1. People who want to manage personal finances effectively.
2. Students tracking their monthly allowance or part-time job earnings.
3. Professionals keeping an eye on income and expenses.
4. Small Business Owners/Freelancers:
5. People who are new to budgeting and want a simple tool to start.


## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Deployment and Development](#deployment-and-development)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Future Enhancements](#future-enhancements)

## Installation
1. the repository template: [Template](https://github.com/Code-Institute-Org/p3-template)
   
2. set up Google Cloud Platform APIs for Google Drive


3. add in the SCOPE `SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive
    ]`

3. Install the required packages: pip install gspread google-auth colorama
   
5. Set up the Google Sheets API Creds add it to the file srrucsher and rename it to `creds.json` 
    - #### Google Sheets API Setup
      1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
      2. Create a new project or select an existing project.
      3. Enable the Google Sheets API and the Google Drive API.
      4. Create credentials:
         - Select "Service account" and follow the prompts.
          - Download the file, place it in your project directory, and rename it `creds.json`.
      5. Share your Google Sheet with the service account email.
  
  6. Put the credits dot Jason file into get dot to ignore to ensure that the sensitive information there is not deployed or pushed to get up as it can contain personal information such as e-mail addresses for your Google Sheets

## Features
- **User-Friendly Interface**: Simple command-line interface for easy interaction and navigation.

![image](https://github.com/user-attachments/assets/85ff3702-432d-4202-b65c-1763295293cc)

- **Data Entry for Income and Expenses**: Allows users to input details for both income and expenses, including:
Date, category, amount, and optional description.

![image](https://github.com/user-attachments/assets/2e84d3a9-1838-48fe-afbe-1d37abce398e)

- **Input Validation**: Ensures accurate and correct data entry with checks for format and numbers.

![image](https://github.com/user-attachments/assets/480b1caf-0cff-4ede-8653-7575818a8484)

- **Google Sheets Integration**: Utilizes Google Sheets for real-time data storage and retrieval.Automatically updates the appropriate worksheet (Income or Expenses) upon data entry.

![image](https://github.com/user-attachments/assets/b9f53b0e-32b7-4b07-8baa-6795331a112c)

- **Financial Reporting**: Generates a summary report of total income, total expenses, and net savings. Provides clear insights into financial. 

![image](https://github.com/user-attachments/assets/d05c7346-3d46-49ad-b632-b40129aeec34)

- **Recent Entries Display**: Displays the five most recent entries from either the Income or Expenses worksheet. Allows users to quickly review their latest financial activities.

![image](https://github.com/user-attachments/assets/67be77e4-4f72-4ad6-b504-08e1c52c5dea)

- **Error Handling**: Catches exceptions during data retrieval and updates, providing informative error messages to users.

![image](https://github.com/user-attachments/assets/48437d76-aeec-41aa-b2eb-7aaa5b721482)

- **Customizable Entry Categories**: Users can input custom categories for income and expenses, enhancing tracking flexibility.

![image](https://github.com/user-attachments/assets/60391f70-29dc-42c5-8cf4-7b56233df62d)

- **Quit Functionality**: Provides an option to exit the application gracefully.

![image](https://github.com/user-attachments/assets/60dcd559-022e-4050-8578-6e4905654a35)

- **Color-Coded Output**: Utilizes the colorama library for color-coded text in the terminal, improving readability and user experience.

![image](https://github.com/user-attachments/assets/9f4fbca6-a8bf-4298-82d4-4b4cd2802ae9)
![image](https://github.com/user-attachments/assets/1bec52e4-8b0c-4a1c-a187-12d378fb2154)
![image](https://github.com/user-attachments/assets/658d290c-1334-412c-8aab-e8000e0951a9)


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

## Testing
Open my code to (https://pep8ci.herokuapp.com/#) Listed several errors in formatting as seen below
 ![image](https://github.com/user-attachments/assets/88696b70-a7ec-4ff3-aaff-fa20ab13d35d)
And so going through 1 by 1 Googling how to fix these errors I reduce them to 0
 ![image](https://github.com/user-attachments/assets/758b4fba-5dea-472c-b333-28fabcb251a9)

Along with the testing for format I also manually tested inputs and they developed nation by in putting all the correct inputs such as date category amount description for income and expenses and the inputs for report and recent do ensure that they came out as desired I then entered incorrect inputs to test the validation for each stage to ensure that only the correct entries could be submitted
## User Options and Expected Outcomes

| **Option**        | **Description**                                                                                          | **Expected Outcome**                                                                                 | **Pass or Fail** |
|--------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------|
| `Income`          | Allows the user to input income data, including date, category, amount, and optional description.         | The data is validated and added to the "Income" worksheet if valid. A success or failure message is displayed. | Pass             |
| `Expense`         | Allows the user to input expense data, including date, category, amount, and optional description.        | The data is validated and added to the "Expenses" worksheet if valid. A success or failure message is displayed. | Pass             |
| `Report`          | Generates a financial report that calculates and displays total income, total expenses, and net savings. | A summary report is printed, showing the user's financial status.                                      | Pass             |
| `Recent`          | Displays the most recent entries (up to 5) from either the "Income" or "Expenses" worksheet.             | The user views the last 5 entries from the selected worksheet, with details formatted neatly.         | Pass             |
| `Quit`            | Exits the program.                                                                                       | A farewell message is displayed, and the program terminates.                                         | Pass             |
| `Invalid Input`      | Handles unrecognized inputs or actions.                                                                 | An error message is displayed, prompting the user to try again.                                       | Pass             |

### Notes:
- **Input Validation:** User inputs (dates, categories, and amounts) are validated to ensure data integrity.
- **Error Handling:** Any issues (e.g., Google Sheets connection errors) are caught and an appropriate error message is displayed.
- **Optional Description:** Users can provide additional details for income or expenses, though this field is not mandatory.

## Troubleshooting
- **Common Issues**:
  - If you encounter issues, ensure the `creds.json` file is in the correct directory and contains valid credentials.
  - Check for internet connectivity when accessing Google Sheets.
  - Review the input validation messages for guidance on correcting any data entry errors.
  - 

## Deployment and Development
### Cloning the Project
1. **Install Git**: If Git isn't already installed, download it from the [Git website](https://git-scm.com/) and follow the setup instructions for your operating system.
2. **Create a Project Folder**: Run the command:
   ```bash
   mkdir budget-tracker
   ```
3. **Navigate to the Project Directory**: Enter the directory:
   ```bash
   cd budget-tracker
   ```
4. **Clone the Repository**: Clone your project repository:
   ```bash
   git clone https://github.com/your-username/budget-tracker.git .
   ```

### Running the Project in the Terminal
1. **Open Terminal**: Navigate to the project folder if you're not already there.
2. **Install Dependencies**: Run the following command to install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**: Start the Budget Tracker by executing:
   ```bash
   python main.py
   ```
   Replace `main.py` with the actual file name that contains the entry point for your project, such as `budget_tracker.py`, if applicable.

### Deployment to Heroku
Make a Heroku Account
  - Heroku Account: Set up an account on Heroku.com.
  - 
setting Up Heroku
  - Create a New App:
      Navigate to the Heroku dashboard and click "Create new app".
      Choose a unique name related to the budget tracker and set your region.
    
Configuration
   - Config Variables:
Use Config Vars to set sensitive data like API keys or creds.json file for API authentication. Enter its contents as a value for a config var in the Heroku app settings.
Deploying from GitHub

Connect to GitHub:
In the "Deploy" tab of your Heroku app, connect your app to your GitHub repository.

Deployment Method:
Choose between automatic deployment (which deploys upon each push to your GitHub repository) or manual deployment from a specified branch to maintain a stable version.

Launch:
Click "Deploy Branch" to start the build process. Heroku will install the required dependencies and launch your application.

Verify Deployment:
Once deployed, open the app's URL to ensure it runs correctly. Test its functionality thoroughly.

## Contact
For questions or feedback, please reach out to me at my [GitHub profile](https://github.com/FinnbarrAmbrose).

## Acknowledgments
- Special thanks to the developers of gspread and colorama for their fantastic libraries that enabled the functionality of this application.
- Special thanks to the love sandwich walk though project help explain the finer details of start and development 
- Special thanks to my GF for helping to make the use expires easier when the user is new to the program 

- ### videos 
    - [Python Tutorial: Using Try/Except Blocks for Error Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8&pp=ygURcHl0aG9uIHRyeSBleGNlcHQ%3D)
    - [Advanced Exception Handling in Python](https://www.youtube.com/watch?v=ZUqGMDppEDs&pp=ygUVcHl0aG9uIGVycm9yIGhhbmRsaW5n)
    - [Colored Console Output in Python](https://www.youtube.com/watch?v=kf8kbUKeM5g&pp=ygUTcHl0aG9uIGNvbG9yZWQgdGV4dA%3D%3D)
    - [Python Tutorial 7 - Formatting Output in Python](https://www.youtube.com/watch?v=Ln5dzg820PU&pp=ygUYcHl0aG9uIG91dHB1dCBmb3JtYXR0aW5n)
    - [Python 101 Python Basics for Beginners Playlist](https://www.youtube.com/watch?v=JTFGllcJ29I&list=PLNnG2akFozlISSPF2UiUFSHieGCc_BA9b).

## Future Enhancements
1. Create a report function that allows users to display financial data for specific dates or months.
2. Improve the recent entries feature to prioritize the most recent date rather than the most recent entry.
3. Implement a multiple-choice category selection for income or expense entries to enhance data filtering in Google Sheets.
4. Add in error handling for negative numbers entered under income and positive numbers entered under Expenses.
