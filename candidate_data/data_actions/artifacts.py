import json
from helpers.logger import Logger


class Artifacts:
    """"Class for handling output reports."""

    def __init__(self) -> None:
        self._logger = Logger().get_logger()

    def save_output(self, candidate_data: list, file_name: str = "output_report.json") -> None:
        """ Save the processed candidate data to JSON file"""
        try:
            with open(file_name, "w") as f:
                json.dump(candidate_data, f, indent=4)
            self._logger.info(f"Report saved to {file_name}")
        
        except Exception as e:
            self._logger.error(f"Error in saving report: {e}")
            raise

    def giveout_resp(self, candidate_data) -> str:
        """Generate a text-based report for candidates."""
        report = ""
        for candidate in candidate_data:
            report += f"Hello {candidate.get('name')},\n"
            for experince in candidate.get('work_experince'):
                report += f"{experince}\n"
            report += "\n"
        return report