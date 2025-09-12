import requests
from helpers.logger import Logger

class DataFetcher:
    """Handles the fetching of candidate data from URL."""

    def __init__(self):
        self._logger = Logger().get_logger()

    def data_fetch(self, url: str) -> dict:
        """Fetching all the data from the provided URL"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            self._logger.info(f"Data fetched successfully from {url}")
            return response.json()
        except requests.exceptions.RequestException as e:
            self._logger.error(f"Error fetching data from {url}: {e}")
            raise
