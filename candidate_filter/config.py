# config.py

class Config:
    """Configuration class to store application settings"""

    URL = "https://hs-recruiting-test-resume-data.s3.amazonaws.com/allcands-full-api_hub_b1f6-acde48001122.json"
    
    DB_URI = "mongodb://localhost:27017/"
    DB_NAME = "local_db"
    DB_COLLECTION = "filtered_candidates"