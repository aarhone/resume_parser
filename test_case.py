import unittest
from unittest.mock import patch
from data_fetcher import DataFetcher

# Mock data for testing
mock_data = [
    {
        "name": "John Doe",
        "industry": "Software",
        "years_of_experience": 5,
        "skills": ["Python", "Django"]
    },
    {
        "name": "Jane Smith",
        "industry": "Finance",
        "years_of_experience": 8,
        "skills": ["Excel", "Accounting"]
    }
]

class TestDataFetcher(unittest.TestCase):

    @patch('requests.get')
    def test_fetch(self, mock_get):
        class MockResponse:
            def json(self):
                return mock_data
        mock_get.return_value = MockResponse()
        
        url = "http://example.com/api/candidates"
        fetcher = DataFetcher(url)
        data = fetcher.fetch()
        
        self.assertEqual(data, mock_data)

if __name__ == '__main__':
    unittest.main()