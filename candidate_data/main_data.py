from helpers.logger import Logger
from data_fetcher import DataFetcher
from data_actions.data_processor import DataProcessor
from data_actions.artifacts import Artifacts
from config import Config


class CandidateDataProcessor:
    """Class to process the data and handle the application."""

    def __init__(self) -> None:
        self._logger = Logger().get_logger()
        self._data_fetcher = DataFetcher()
        self._data_processor = DataProcessor()
        self._artifacts = Artifacts()

    def run(self, url: str) -> None:
        try:
            self._logger.info("Starting candidate data processing.")

            # Fetching data from URL.
            data = self._data_fetcher.data_fetch(url)

            # Process candidate information.
            candidate_data = [self._data_processor.process_candidate(candidate) for candidate in data]

            # Generating rquired output.
            self._artifacts.save_output(candidate_data)
            print(self._artifacts.giveout_resp(candidate_data))

            self._logger.info("candidate data processing completed successfully.")

        except Exception as e:
            self._logger.error(f"An error occured: {e}")
            raise


if __name__ == "__main__":
    starter = CandidateDataProcessor()
    url = Config.URL
    starter.run(url)
