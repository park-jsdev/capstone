import pandas as pd
import pytest

# Pytest combines setup, execute, and teardown with fixtures.
# Usage: Export the test data csv file and the output data csv file from Power BI,
#        python -m pytest test_resolution_time_csv.py --test_data_file=<path_to_test_data_file> --output_data_file=<path_to_output_data_file>
#        Replace <path_to_test_data_file> and <path_to_output_data_file> with the paths to the test data and output data csv file.

import pandas as pd
import pytest

# Define the column names as variables
START_DATE_COL = 'Start Date'
END_DATE_COL = 'End Date'
EXPECTED_AVG_RES_TIME_COL = 'Expected Avg Resolution Time'
MONTHS_COL = 'Months'
EXPECTED_AVG_COL = 'Expected Avg'

# Fixture to load the test data csv file
@pytest.fixture
def test_data(test_data_file):
    return pd.read_csv(test_data_file)

# Fixture to load the output data csv file
@pytest.fixture
def output_data(output_data_file):
    return pd.read_csv(output_data_file)

# test the output's average resolution time vs the actual resolution time from the test data
def test_average_resolution_time_total(test_data, output_data):
    days_diff = (pd.to_datetime(test_data[END_DATE_COL]) - pd.to_datetime(test_data[START_DATE_COL])).dt.days
    avg_days_diff = days_diff.mean()
    expected_avg_days_diff = output_data[EXPECTED_AVG_RES_TIME_COL].iloc[0]
    assert avg_days_diff == pytest.approx(expected_avg_days_diff, rel=1e-2)

# test the output's average resolution time per month vs the actual resolution time per month from the test data
def test_average_resolution_time_per_month(test_data, output_data):
    # Convert date columns to datetime type
    test_data[START_DATE_COL] = pd.to_datetime(test_data[START_DATE_COL])
    test_data[END_DATE_COL] = pd.to_datetime(test_data[END_DATE_COL])
    
    # Calculate days difference and group by month
    test_data['Days Difference'] = (test_data[END_DATE_COL] - test_data[START_DATE_COL]).dt.days
    grouped = test_data.groupby(test_data[START_DATE_COL].dt.month)['Days Difference']

    # Calculate actual average for each month
    actual_avg_days_diff_per_month = grouped.mean()

    # Check if the calculated values match the expected values
    expected_avg_days_diff_per_month = output_data.set_index(MONTHS_COL)[EXPECTED_AVG_COL].to_dict()
    assert actual_avg_days_diff_per_month.to_dict() == pytest.approx(expected_avg_days_diff_per_month, rel=1e-2)