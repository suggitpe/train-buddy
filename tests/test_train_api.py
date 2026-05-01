"""
Tests for the placeholder train API client.
"""
import unittest

# This import will fail initially, which is expected for TDD
from src.train_api import get_train_service

class TestTrainApiClient(unittest.TestCase):
    """
    Test suite for the placeholder train API client.
    """

    def test_get_train_service_placeholder(self):
        """
        Tests that the placeholder function returns a hardcoded data structure.
        """
        service_id = "C12345"
        expected_data = {
            "service_id": "C12345",
            "std": "06:36",
            "etd": "On time",
            "origin": "Kettering",
            "destination": "St Pancras"
        }

        actual_data = get_train_service(service_id)

        self.assertEqual(actual_data, expected_data)

if __name__ == '__main__':
    unittest.main()
