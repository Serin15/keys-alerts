# Selenium WebDriver Test Project

## Description
This project uses **Selenium WebDriver** together with **unittest** to test interaction with JavaScript alerts and keyboard input on a web page.

## Project Structure
- **alerts.py** - Tests for JavaScript alerts
- **keys.py** - Tests for keyboard interaction
- **test_suite.py** - Test suite to run multiple test cases together

## Setup
### 1. Install Dependencies
To run the tests, install all necessary packages using the command:
```sh
pip install selenium
```

### 2. Download WebDriver
Ensure you have installed **geckodriver** for Firefox or **chromedriver** for Chrome and that it is in the system PATH.

## Running the Tests
To run the tests, use the following commands:

### JavaScript Alerts Tests:
```sh
python -m unittest alerts.py
```

### Keyboard Interaction Tests:
```sh
python -m unittest keys.py
```

### Running the Full Test Suite:
```sh
python test_suite.py
```

## Author
Created by Ali Serin
