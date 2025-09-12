import json
import argparse
from logger.logger import Logger
from data_fetcher import DataFetcher
from config import Config
from filter_actions.candidate_filter import CandidateSort
from filter_actions.get_candidatedata import FetchCandidateData
from mongodb_setup import MongoDBconnection

class ArgumentParser:
    """Class to handle argument parsing."""

    @staticmethod
    def parse_arguments():
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(description="Criteria to select candidates")
        parser.add_argument("--industry", type=str, help="Experience in a certain industry", default=None)
        parser.add_argument("--skills", type=str, nargs='+', help="List of specific skills required (In double quotes space separated)", default=[])
        parser.add_argument("--min_exp", type=int, help="Minimum total years of experience", default=None)
        return parser.parse_args()

class CandidateFilter:
    """Class to process the data and handle the application."""

    def __init__(self) -> None:
        self._logger = Logger().get_logger()
        self._data_fetcher = DataFetcher()
        self._get_candidatedata = FetchCandidateData()
        self._mongo_db = MongoDBconnection()

    def fetch_and_process_data(self, url):
        """Fetch and process candidate data from the URL."""
        try:
            response_data = self._data_fetcher.data_fetch(url)
            candidate_info = [self._get_candidatedata.process_candidateinfo(candidate) for candidate in response_data]
            return candidate_info
        except Exception as e:
            self._logger.error(f"Error fetching or processing data: {e}")
            return []

    def filter_candidates(self, candidate_info, industry, skills, min_experience):
        """Filter candidates based on the given criteria."""
        try:
            candidate_filter = CandidateSort(candidate_info)
            selected_candidates = candidate_filter.main_filter(
                industry=industry,
                skills=skills,
                min_experience=min_experience
            )
            return selected_candidates
        except Exception as e:
            self._logger.error(f"Error filtering candidates: {e}")
            return []

    def insert_candidates_to_db(self, selected_candidates):
        """Insert selected candidates into MongoDB."""
        try:
            self._mongo_db.inserting_transformed_data(selected_candidates)
        except Exception as e:
            self._logger.error(f"Error inserting candidates into MongoDB: {e}")

    def run(self, url):
        """Application driver code."""
        args = ArgumentParser.parse_arguments()
        candidate_info = self.fetch_and_process_data(url)
        selected_candidates = self.filter_candidates(candidate_info, args.industry, args.skills, args.min_exp)
        with open('inserted_Candidate_data.json', 'w') as json_file:
            json.dump(selected_candidates, json_file, indent=4)
        self.insert_candidates_to_db(selected_candidates)

if __name__ == "__main__":
    starter = CandidateFilter()
    starter.run(Config.URL)