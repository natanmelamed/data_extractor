import pathlib
from datetime import datetime

from common_utils import (
    load_data_from_json_file,
    convert_str_date_to_datetime,
    save_json_file_with_new_content,
)


class DataExtractor:
    DATE_LIST: dict = ["value1", "value4"]

    def __init__(self, path: pathlib.Path):
        self.python_exercise_data: dict = load_data_from_json_file(file_path=path)
        self.processed_data: dict = {}
        self.values_keys_list: list = ["value2", "value3"]

    def data_processor(self) -> None:
        for current_value in self.DATE_LIST:
            current_datetime_date: datetime = convert_str_date_to_datetime(
                self.python_exercise_data[current_value], 2021
            )
            self.processed_data[current_value] = current_datetime_date
        self.processed_data[self.values_keys_list[0]]: str = self.python_exercise_data[
                                                                 self.values_keys_list[0]
                                                             ].replace(" ", "")[::-1]
        self.processed_data[self.values_keys_list[1]] = list(
            set(self.python_exercise_data[self.values_keys_list[1]])
        )
        save_json_file_with_new_content("processed_data.json", self.processed_data)
