# Python Automation Script with Selenium

This project automates tasks in a web-based interface using Selenium WebDriver. The script performs actions such as logging into a system, navigating through pages, selecting options, downloading files, and processing downloaded data.

<video src="https://github.com/arizmuajianisan/python-automation-selenium/blob/ff5fa11bde9b365e4ed0469751852adedf76fb81/result.mp4" width="640"/>

## Features

- **Automated Web Interaction**: Logs into a web application, navigates through pages, and performs actions such as form submissions, checkbox selections, and file downloads.
- **File Handling**: Monitors the download directory for the completion of ZIP file downloads.
- **Data Extraction**: Extracts the contents of downloaded ZIP files into a specified directory.
- **Data Merging**: Merges all CSV files from the extracted ZIP files into a single CSV file.
- **Directory Cleaning**: Cleans up the working directory by deleting unnecessary `.csv` and `.tmp` files.

## Prerequisites

- Python >= 3.10
- `pip` (Python package installer)
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/arizmuajianisan/python-automation-selenium.git
   cd python-automation-selenium
   ```
2. **Create a Virtual Environment**:
   **venv**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

   **conda** I'm using Conda, btw. It will create env-autonatio with the following packages installed
   ```bash
   conda env create -f environment.yml
   ```

## Usage

1. Configuration
   - URL Configuration: Modify the url, login_page, and data_output_page variables in the script to match your target web application's URLs.
   - User Credentials: Set the username and password variables in the .env with the credentials required to log in.
   - Make sure the date start for selection form that wanted to be downloaded
2. Running the Script
   ```bash
   python main.selenium.py
   ```
3. Monitoring Download
   The script will automatically detect when the ZIP file download is complete. After that, it will extract the contents of the ZIP file, merge all CSV files into a single file, and then clean up the directory by removing unnecessary files.
4. Cleaning the Directory
   After processing, you can manually clean up the directory by running:
   ```bash
   python clean_directory.py
   ```

## Project Structure
```bash
.
├── main.py                # Main script for automation
├── requirements.txt       # Python dependencies
├── README.md              # This readme file
├── chromedriver           # ChromeDriver executable (or it can be placed elsewhere in PATH)
└── env/                   # Virtual environment directory (optional)
```

## Functions Overview
- **initialize_browser()**: Initializes the Selenium WebDriver.
- **login(browser)**: Logs into the web application using provided credentials.
- **navigate_and_perform_tasks()**: Performs the necessary tasks on the web application.
- **monitor_download()**: Monitors the download directory for ZIP file completion.
- **extract_zip()**: Extracts the contents of the downloaded ZIP file.
- **merge_csv_files()**: Merges all CSV files into a single file.
- **clean_directory()**: Cleans up the directory by deleting unnecessary files.

## Acknowledgments
- Selenium WebDriver for browser automation.
- Python's os, time, and zipfile modules for file handling.
- The open-source community for various tutorials and guides.