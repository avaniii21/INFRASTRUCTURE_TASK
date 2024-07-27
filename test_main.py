import unittest
import pandas as pd
from pandas.testing import assert_series_equal
from main import calculate_total_revenue, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_10_customers

class TestMain(unittest.TestCase):

    def setUp(self):
        data = {
            'order_id': [1, 2, 3],
            'customer_id': [1, 2, 1],
            'order_date': ['2021-01-01', '2021-01-02', '2021-02-01'],
            'product_id': [1, 2, 1],
            'product_name': ['Product A', 'Product B', 'Product A'],
            'product_price': [100, 200, 100],
            'quantity': [1, 2, 1]
        }
        self.df = pd.DataFrame(data)
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])

    def test_calculate_total_revenue(self):
        result = calculate_total_revenue(self.df)
        expected_revenue = pd.Series([100, 400, 100], name='total_revenue')
        assert_series_equal(result['total_revenue'], expected_revenue)

    def test_compute_monthly_revenue(self):
        self.df = calculate_total_revenue(self.df)
        result = compute_monthly_revenue(self.df)
        expected = pd.Series([500, 100], index=pd.PeriodIndex(['2021-01', '2021-02'], freq='M'), name='total_revenue')
        expected.index.name = 'month'
        assert_series_equal(result, expected)

    def test_compute_product_revenue(self):
        self.df = calculate_total_revenue(self.df)
        result = compute_product_revenue(self.df)
        expected = pd.Series([200, 400], index=pd.Index(['Product A', 'Product B'], name='product_name'), name='total_revenue')
        assert_series_equal(result, expected)

    def test_compute_customer_revenue(self):
        self.df = calculate_total_revenue(self.df)
        result = compute_customer_revenue(self.df)
        expected = pd.Series([200, 400], index=pd.Index([1, 2], name='customer_id'), name='total_revenue')
        assert_series_equal(result, expected)

    def test_top_10_customers(self):
        self.df = calculate_total_revenue(self.df)
        result = top_10_customers(self.df)
        expected = pd.Series([400, 200], index=pd.Index([2, 1], name='customer_id'), name='total_revenue')
        assert_series_equal(result, expected)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

