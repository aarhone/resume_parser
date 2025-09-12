from datetime import datetime
from helpers.logger import Logger
from helpers.utils import Utils


class DataProcessor:
    """Class to process candidate data, calculate job gaps and format"""
    def __init__(self) -> None:
        self._logger = Logger().get_logger()

    def _calculate_gap(self, before_start_date: datetime, current_end_date: datetime) -> int:
        """Method to calculate the gap between two jobs."""
        if current_end_date and before_start_date:
            gap_days = (before_start_date - current_end_date).days
            return gap_days if gap_days > 0 else 0
        
        return 0

    def _process_job(self, job_data: dict) -> list:
        """Method to format job experince data."""
        role = job_data.get("title", "Unknow Role")
        start_date_str = job_data.get("start_date", "")
        end_date_str = job_data.get("end_date", "")
        location = job_data.get("location", "").get("short_display_address", "Unknown Location")

        start_date = Utils.parse_date(start_date_str)
        end_date = Utils.parse_date(end_date_str)

        return [start_date, end_date, role, location]

    def process_candidate(self, candidate_data: dict) -> dict:
        """Method to process work experince for a candidate"""
        name = candidate_data.get("contact_info", {}).get("name", {}).get("formatted_name", "Unknown candidate")
        work_experince_data = candidate_data.get("experience", [])

        self._logger.info(f"Processing candidate : {name}")

        work_experince, formatted_job = [], []

        for job_data in work_experince_data:
            formatted_job.append(self._process_job(job_data))
        formatted_job.sort(reverse=True)
        
        if formatted_job:
            for i in range(len(formatted_job)-1):
                work_experince.append(f"Worked as: {formatted_job[i][2]}, From {Utils.date_convertor(formatted_job[i][0])} To {Utils.date_convertor(formatted_job[i][1])} in {formatted_job[i][3]}")
                gap_days = self._calculate_gap(formatted_job[i][0], formatted_job[i+1][1])
                if gap_days > 0:
                    self._logger.info(f"Gap in CV for {gap_days} days found between jobs.")
                    work_experince.append(f"Gap in CV for {gap_days} days")

            work_experince.append(f"Worked as: {formatted_job[-1][2]}, From {Utils.date_convertor(formatted_job[-1][0])} To {Utils.date_convertor(formatted_job[-1][1])} in {formatted_job[-1][3]}")
        
        else:
            work_experince.append("No prior work experince")

        return {"name": name, "work_experince": work_experince}