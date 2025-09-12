from logger.logger import Logger


class FetchCandidateData:
    """Class to process candidate data, calculate job gaps and format"""
    def __init__(self) -> None:
        self._logger = Logger().get_logger()

    def _process_experince(self, exp_data):
        try:
            experince_month = int(exp_data.get("duration_in_month", "0"))
            industry = exp_data.get("company_details", {}).get("industry", "") if exp_data.get("company_details") else None
            return experince_month, industry
        except Exception as e:
            self._logger.error(f"Unexpected error in _process_experince: {e}")
        return 0, None

    def process_candidateinfo(self, candidate_data: dict) -> dict:
        """Method to process work experince and skills of a candidate"""
        try:
            # Candidate name.
            name = candidate_data.get("contact_info", {}).get("name", {}).get("formatted_name", "Unknown candidate")

            # All the skills of candidate.
            total_skills = set()
            total_skills.update(candidate_data.get("extracted_skills", []))
            total_skills.update([rs.get("name") for rs in candidate_data.get("resume_skills")])

            work_experince_data = candidate_data.get("experience", [])
            total_exp = 0
            industries = set()

            for job_data in work_experince_data:
                exp, industry = self._process_experince(job_data)
                total_exp += exp
                if industry:
                    industries.add(industry)

            return {
                "name": name,
                "industry": list(filter(None, industries)) if industries else None,
                "skills": list(filter(None, total_skills)) if total_skills else None,
                "total_experince_years": round(float(total_exp / 12), 1)
            }
        except Exception as e:
            self._logger.error(f"Unexpected error in process_candidateinfo: {e}")
            return {"name": "Unknown candidate", "skills": None, "industry": None, "total_experince_years": 0}