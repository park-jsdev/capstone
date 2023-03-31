# Pytest combines setup, execute, and teardown with fixtures.
# Usage: Export the test data csv file and the output data csv file from Power BI,
#        Define the file names in the constants in the test,
#        python -m pytest test_resolution_time_csv.py, or
#        python -m pytest to run all tests

import pandas as pd
import pytest

# Define constants for relative tolerance
REL_TOL = 1e-2

# Define the file names as variables
TEST_DATA_FILE = 'test_data.csv'
OUTPUT_DATA_FILE = 'output_data.csv'

# Define the column names as variables
START_DATE_COL = 'Start Date'
END_DATE_COL = 'End Date'
EXPECTED_AVG_RES_TIME_COL = 'Expected Avg Resolution Time'
MONTHS_COL = 'Months'

# Fixture to load the test data csv file
@pytest.fixture
def test_data():
    return pd.read_csv(TEST_DATA_FILE)

# Fixture to load the output data csv file
@pytest.fixture
def output_data():
    return pd.read_csv(OUTPUT_DATA_FILE)

def test_average_resolution_time_total(test_data, output_data):
    # Drop missing values from the test data
    test_data_clean = test_data.dropna(subset=[START_DATE_COL, END_DATE_COL])
    
    # Calculate days difference and average resolution time for non-missing values
    days_diff = (pd.to_datetime(test_data_clean[END_DATE_COL]) - pd.to_datetime(test_data_clean[START_DATE_COL])).dt.days
    avg_days_diff = days_diff.mean()
    
    # Check if the calculated average matches the expected value
    expected_avg_days_diff = output_data[EXPECTED_AVG_RES_TIME_COL].iloc[0]
    assert avg_days_diff == pytest.approx(expected_avg_days_diff, rel=REL_TOL)

