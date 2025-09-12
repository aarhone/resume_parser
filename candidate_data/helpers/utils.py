from datetime import datetime


class Utils:
    """Helper class for utillity functions"""

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """Parse date string into a datetime object."""
        try:
            return datetime.strptime(date_str, "%b/%d/%Y")
        except ValueError:
            return None
    
    def date_convertor(date_obj: datetime) -> str:
        """Parse date string into a datetime object."""
        try:
            return date_obj.strftime("%b/%d/%Y")
        except ValueError:
            return None