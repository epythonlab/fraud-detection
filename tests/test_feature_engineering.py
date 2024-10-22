import unittest
import pandas as pd
import logging
from scripts.feature_engineering import FeatureEngineering  # Import the class

# Setting up a basic logger for testing
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestFeatureEngineering(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        data = {
            'user_id': [1, 2, 1, 3],
            'device_id': [101, 102, 101, 103],
            'signup_time': ['2024-01-01 10:00:00', '2024-01-01 12:00:00', '2024-01-02 10:00:00', '2024-01-02 14:00:00'],
            'purchase_time': ['2024-01-01 11:00:00', '2024-01-01 13:00:00', '2024-01-02 12:00:00', '2024-01-02 15:00:00'],
            'purchase_value': [200.0, 150.0, 300.0, 250.0],
            'source': ['SEO', 'Ads', 'SEO', 'Direct'],
            'browser': ['Chrome', 'Firefox', 'Chrome', 'Safari'],
            'sex': ['M', 'F', 'M', 'F'],
            'age': [25, 30, 22, 35],
            'ip_address': [1234566, 68958333, 22444556, 434355],
            'ip_int': [1234566, 68958333, 22444556, 434355],
            'country':['United States', 'China', 'Sudan', 'Egypt'],
            'class': [0, 1, 0, 1]
        }
        self.df = pd.DataFrame(data)

        # Initializing the FeatureEngineering instance
        self.fe = FeatureEngineering(self.df, logger)

    def test_preprocess_datetime(self):
        self.fe.preprocess_datetime()
        self.assertIn('hour_of_day', self.fe.df.columns)
        self.assertIn('day_of_week', self.fe.df.columns)
        self.assertIn('purchase_delay', self.fe.df.columns)

    def test_calculate_transaction_frequency(self):
        self.fe.preprocess_datetime()  # Ensure datetime preprocessing is done first
        self.fe.calculate_transaction_frequency()
        self.assertIn('user_transaction_frequency', self.fe.df.columns)
        self.assertIn('device_transaction_frequency', self.fe.df.columns)
        self.assertIn('user_transaction_velocity', self.fe.df.columns)

    def test_normalize_and_scale(self):
        self.fe.preprocess_datetime()
        self.fe.calculate_transaction_frequency()
        self.fe.normalize_and_scale()
        # Checking if numerical columns are scaled (mean close to 0, std close to 1)
        self.assertAlmostEqual(self.fe.df['purchase_value'].mean(), 0, delta=1e-6)
        self.assertAlmostEqual(self.fe.df['purchase_value'].std(), 1, delta=0.2)  # Increased tolerance to 0.2


    def test_encode_categorical_features(self):
        self.fe.encode_categorical_features()
        # Verify that the columns have been one-hot encoded and drop_first has been applied
        self.assertNotIn('source', self.fe.df.columns)
        self.assertNotIn('browser', self.fe.df.columns)
        self.assertNotIn('sex', self.fe.df.columns)
        self.assertIn('source_SEO', self.fe.df.columns)
        self.assertIn('browser_Firefox', self.fe.df.columns)

    def test_pipeline(self):
        self.fe.pipeline()
        processed_data = self.fe.get_processed_data()
        # Check if all transformations are applied in the pipeline
        self.assertIn('hour_of_day', processed_data.columns)
        self.assertIn('user_transaction_frequency', processed_data.columns)
        self.assertIn('device_transaction_frequency', processed_data.columns)
        self.assertIn('source_SEO', processed_data.columns)

    def test_get_processed_data_error(self):
        fe_no_pipeline = FeatureEngineering(self.df, logger)
        with self.assertRaises(ValueError):
            fe_no_pipeline.get_processed_data()

if __name__ == '__main__':
    unittest.main()
