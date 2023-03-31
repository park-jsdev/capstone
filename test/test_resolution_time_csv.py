import pandas as pd
import pytest

# Pytest combines setup, execute, and teardown with fixtures
@pytest.fixture
def test_data():
    return pd.read_csv('test_data.csv')

def test_average_resolution_time_total(test_data):
    days_diff = (pd.to_datetime(test_data['End Date']) - pd.to_datetime(test_data['Start Date'])).dt.days
    avg_days_diff = days_diff.mean()
    overall_avg_days_diff = test_data['Avg Resolution Time'].iloc[0]
    assert avg_days_diff == pytest.approx(overall_avg_days_diff, rel=1e-2)

def test_average_resolution_time_per_month(test_data):
    # Convert date columns to datetime type
    test_data['Start Date'] = pd.to_datetime(test_data['Start Date'])
    test_data['End Date'] = pd.to_datetime(test_data['End Date'])
    
    # Calculate days difference and group by month
    test_data['Days Difference'] = (test_data['End Date'] - test_data['Start Date']).dt.days
    grouped = test_data.groupby(test_data['Start Date'].dt.month)['Days Difference']
    
    # Calculate actual average for each month
    actual_avg_days_diff_per_month = grouped.mean()
    
    # Check if the calculated values match the expected values
    assert actual_avg_days_diff_per_month.to_dict() == pytest.approx(test_data.set_index('Month')['Expected Avg'].to_dict(), rel=1e-2)