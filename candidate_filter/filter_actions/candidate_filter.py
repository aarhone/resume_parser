from logger.logger import Logger

class CandidateSort:
    def __init__(self, candidates):
        self.candidates = candidates
        self.out = []
        self.logger = Logger().get_logger()
    
    def industry_filter(self, industry):
        """Sort by industry."""
        try:
            for candidate in self.candidates:
                if industry in candidate["industry"]:
                    self.out.append(candidate)
        except Exception as e:
            self.logger.error(f"Unexpected error in industry_filter: {e}")
        
    def skills_filter(self, skills):
        """Sort by required skills"""
        try:
            for candidate in self.candidates:
                if all(skill in candidate["skills"] for skill in skills):
                    self.out.append(candidate)
        except Exception as e:
            self.logger.error(f"Unexpected error in skills_filter: {e}")
    
    def min_experience_filter(self, min_experience):
        """Sort by minimum experience."""
        try:
            for candidate in self.candidates:
                if round(min_experience, 1) <= candidate["total_experince_years"]:
                    self.out.append(candidate)
        except Exception as e:
            self.logger.error(f"Unexpected error in min_experience_filter: {e}")

    def main_filter(self, industry=None, skills=None, min_experience=None):
        """Combination of filters."""
        self.out = []
        if industry:
            self.industry_filter(industry)
            self.candidates = list(self.out)
            self.out = []
        if skills:
            self.skills_filter(skills)
            self.candidates = list(self.out)
            self.out = []
        if min_experience >= 0:
            self.min_experience_filter(min_experience)
        
        return self.out