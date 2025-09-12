import logging


class Logger:
	def __init__(self) -> None:
		self._logger = logging.getLogger("candidate_checker")
		self._logger.setLevel(logging.INFO)
		self._setup_file_handler()

	def _setup_file_handler(self):
		file_handler = logging.FileHandler("candidate_checker.log")
		file_handler.setLevel(logging.INFO)

		formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
		file_handler.setFormatter(formatter)

		self._logger.addHandler(file_handler)

	def get_logger(self):
		return self._logger