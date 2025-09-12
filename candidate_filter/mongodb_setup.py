from pymongo import MongoClient
from logger.logger import Logger
from config import Config

class MongoDBconnection:
    def __init__(self) -> None:
        self._logger = Logger().get_logger()
        try:
            self.__client = MongoClient(Config.DB_URI)
            self.__db = self.__client[Config.DB_NAME]
            self._collection = self.__db[Config.DB_COLLECTION]
        except Exception as e:
            self._logger.error(f"Error initializing MongoDB connection: {e}")
    
    def inserting_transformed_data(self, selected_candidates):
        """Inserting filtered candidates to MongoDB"""
        if selected_candidates:
            try:
                self._collection.insert_many(selected_candidates)
                self._logger.info(f"Inserted {len(selected_candidates)} selected candidates into MongoDB")
                print(f"**Inserted {len(selected_candidates)} selected candidates into MongoDB**")
            except Exception as e:
                self._logger.error(f"Error inserting candidates into MongoDB: {e}")
                print("**Error inserting candidates into MongoDB**")
        else:
            self._logger.warning("No candidates found.")
            print("**No candidates found**")
