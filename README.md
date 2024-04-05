# security_clearance
Investigation Hitlist Generator

Description:

This Python script generates an investigation hitlist based on date criteria from an Excel file containing subject data.

Prerequisites:

Python 3.x
Pandas
NumPy

Usage:

1. Place Excel File: Place your Excel file containing subject data (Subject_Report.xlsx) in the same directory as the Python script.
2. Run Script: Execute the Python script generate_hitlist.py:
3. Output: The script will generate an Excel file named Investigation_hitlist.xlsx containing the filtered names.

Customization:

Todays Date: By default, the script uses a predetermined date (2023-10-23). You can modify this date in the script (todays_date variable) to match the current date when running the script.

File Structure:

- generate_hitlist.py: Python script for generating the investigation hitlist.
- Subject_Report.xlsx: Excel file containing subject data (replace with your own file).
- Investigation_hitlist.xlsx: Output Excel file containing the filtered names.

Dependencies:

Pandas: Python library for data manipulation and analysis.
NumPy: Python library for numerical computing.