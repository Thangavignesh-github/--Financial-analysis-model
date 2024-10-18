
# Financial Analysis Model

## Overview

The Financial Analysis Model is a Python-based application designed to evaluate various financial metrics for businesses using their financial data. The model processes financial data and generates flags that indicate the company's financial health based on specific criteria. This project is useful for financial analysts and decision-makers looking to assess company performance.

## Features

- **Financial Flag Evaluation**: Calculates financial flags such as total revenue, borrowing to revenue ratio, and Interest Service Coverage Ratio (ISCR).
- **Data Input**: Accepts financial data in JSON format.
- **User-Friendly Interface**: Provides a web-based interface for data submission and result display.

## Components

- `model.py`: The main script that processes financial data and evaluates flags.
- `rules.py`: Contains the logic for calculating various financial metrics.
- `data.json`: Sample data file used for testing the model.
- `app.py`: The Flask application that provides a web interface for users.
- `templates/`: Directory containing HTML templates for the web application.
  - `upload.html`: The page for uploading the financial data file.
  - `results.html`: The page for displaying the results.

## Prerequisites

- Python 3.11 or higher
- Flask
- Additional Python libraries as needed (see requirements.txt)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd financial-analysis-model
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the project structure:
   - Ensure the following directory structure:
     ```
     financial-analysis-model/
     ├── app.py
     ├── model.py
     ├── rules.py
     ├── data.json
     ├── requirements.txt
     └── templates/
         ├── upload.html
         └── results.html
     ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. Upload your financial data JSON file by clicking on the "Choose File" button and then click "Submit".

4. The application will process the file and display the results on the next page.



## Error Handling

The application includes error handling to manage issues such as:

- File upload errors
- Validation of JSON structure
- Server-side validation of financial data
