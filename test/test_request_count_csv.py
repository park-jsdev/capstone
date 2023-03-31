# This test will by default set the relative tolerance to 3 times the standard deviation by default by the 3 Sigma Rule.
# This is useful for when the expected values are not known with high precision.
# You can comment it out if you want to specify your own relative tolerance. Relative accuracy typically uses 1%.
#
# Pytest combines setup, execute, and teardown with fixtures.
# Usage: Export the test data csv file and the output data csv file from Power BI,
#        Define the file names in the constants in the test,
#        python -m pytest test_request_count_csv.py, or
#        python -m pytest to run all tests

import pandas as pd
import pytest
import numpy as np

# Define constants for relative tolerance
REL_TOL = 1e-2

# Define the file names as variables
TEST_DATA_FILE = 'test_data.csv'
OUTPUT_DATA_FILE = 'output_data.csv'

# Define the column names as variables
EXPECTED_TOTAL_ROWS = 'Expected Count'

# Fixture to load the test data csv file
@pytest.fixture
def test_data():
    return pd.read_csv(TEST_DATA_FILE)

# Fixture to load the output data csv file
@pytest.fixture
def output_data():
    return pd.read_csv(OUTPUT_DATA_FILE)

# Calculate the standard deviation of the data, you need to get standard deviation across all rows, hence axis param
std_dev = np.std(test_data.values, axis=1)

# Set the relative tolerance as three times the standard deviation (For high uncertainty)
REL_TOL = 3 * std_dev

# Test total rows
def test_total_rows(test_data, output_data):
    # Load the test data and output data CSV files
    test_data = pd.read_csv(TEST_DATA_FILE)
    output_data = pd.read_csv(OUTPUT_DATA_FILE)

    # Check if the number of rows in the test data matches the number of rows in the output data
    expected_total_rows = output_data[EXPECTED_TOTAL_ROWS].iloc[0]
    actual_rows_count = len(test_data)
    assert actual_rows_count == expected_total_rows, f"Error: Row count does not match. Expected: {expected_total_rows}, Actual: {actual_rows_count}."
