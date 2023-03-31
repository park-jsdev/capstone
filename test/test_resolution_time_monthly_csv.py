# Pytest combines setup, execute, and teardown with fixtures.
# Usage: Export the test data csv file and the output data csv file from Power BI,
#        Define the file names in the constants in the test,
#        python -m pytest test_resolution_time_monthly_csv.py, or
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
MONTHS_COL = 'Months'
EXPECTED_AVG_COL = 'Expected Avg'

# Fixture to load the test data csv file
@pytest.fixture
def test_data():
    return pd.read_csv(TEST_DATA_FILE)

# Fixture to load the output data csv file
@pytest.fixture
def output_data():
    return pd.read_csv(OUTPUT_DATA_FILE)

# test the output's average resolution time per month vs the actual resolution time per month from the test data
def test_average_resolution_time_per_month(test_data, output_data):
    # Convert date columns to datetime type
    test_data[START_DATE_COL] = pd.to_datetime(test_data[START_DATE_COL])
    test_data[END_DATE_COL] = pd.to_datetime(test_data[END_DATE_COL])
    
    # Add Days Difference column to the original DataFrame
    test_data.loc[test_data[START_DATE_COL].notnull() & test_data[END_DATE_COL].notnull(), 'Days Difference'] = (test_data[END_DATE_COL] - test_data[START_DATE_COL]).dt.days
    
    # Calculate days difference and group by month
    grouped = test_data.groupby(test_data[START_DATE_COL].dt.month)['Days Difference']

    # Calculate actual average for each month
    actual_avg_days_diff_per_month = grouped.mean()

    # Check if the calculated values match the expected values
    expected_avg_days_diff_per_month = output_data.set_index(MONTHS_COL)[EXPECTED_AVG_COL].to_dict()
    assert actual_avg_days_diff_per_month.to_dict() == pytest.approx(expected_avg_days_diff_per_month, rel=REL_TOL)
