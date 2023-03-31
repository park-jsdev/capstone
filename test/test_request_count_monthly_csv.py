# Pytest combines setup, execute, and teardown with fixtures.
#
# Good Rule of thumb is to set the relative tolerance to 3 times the standard deviation by default by the 3 Sigma Rule.
# This is useful for when the expected values are not known with high precision.
# Relative accuracy typically uses 1%.
#
# Usage: Export the test data csv file and the output data csv file from Power BI,
#        Define the file names in the constants in the test,
#        python -m pytest test_request_count_monthly_csv.py, or
#        python -m pytest to run all tests

import pandas as pd
import pytest

# Define constants for relative tolerance
REL_TOL = 1e-2

# Define the file names as variables
TEST_DATA_FILE = 'test_data.csv'
OUTPUT_DATA_FILE = 'output_data.csv'

# Define the column names as variables
DATE_COL = 'Date Logged'
MONTHS_COL = 'Months'
EXPECTED_COUNT_COL = 'Expected Count'

# Fixture to load the test data csv file
@pytest.fixture
def test_data():
    return pd.read_csv(TEST_DATA_FILE)

# Fixture to load the output data csv file
@pytest.fixture
def output_data():
    return pd.read_csv(OUTPUT_DATA_FILE)

# Test count per month
def test_count_per_month(test_data, output_data):
    # Load the test data and output data CSV files
    test_data = pd.read_csv(TEST_DATA_FILE)
    output_data = pd.read_csv(OUTPUT_DATA_FILE)

    # Convert the date column to datetime type
    test_data[DATE_COL] = pd.to_datetime(test_data[DATE_COL])

    # Group the data by month based on the date column
    grouped = test_data.groupby(test_data[DATE_COL].dt.month)[DATE_COL]

    # Calculate actual count for each month
    actual_count_per_month = grouped.count()

    # Check if the calculated values match the expected values
    expected_count_per_month = output_data.set_index(MONTHS_COL)[EXPECTED_COUNT_COL].to_dict()
    assert actual_count_per_month.to_dict() == pytest.approx(expected_count_per_month, rel=REL_TOL)
