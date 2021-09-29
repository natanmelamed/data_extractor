import json
import datetime
from dateutil import parser
from collections import OrderedDict
from typing import Union, Optional

TIME_FORMAT: str = "%Y/%m/%d %H:%M:%S"


def load_data_from_json_file(
        file_path: str,
) -> Optional[Union[list, dict, int, str, bool]]:
    try:
        with open(file_path, "r") as json_file:
            if isinstance(json_file, list):
                data = json.loads(json.dumps(json_file))
            else:
                data = json.load(json_file, object_pairs_hook=OrderedDict)
    except Exception as e:
        print("Bad input:\n\n" + str(e) + "\n\n")
    return data


def save_json_file_with_new_content(
        file_path: str, json_content: Optional[Union[list, dict, int, str, bool]]
) -> None:
    with open(file_path, "w") as json_file:
        if isinstance(json_content, list):
            json_content = json.loads(json.dumps(json_content))
        json.dump(json_content, json_file, indent=2)


def convert_str_date_to_datetime(date: str, year: int) -> datetime:
    date: datetime = parser.parse(date).replace(year=year)
    return date.strftime(TIME_FORMAT)


def sort_dict_by_keys(dictionary: dict) -> dict:
    return {key: value if not isinstance(value, list) else sort_mix_list(value) for key, value
            in dictionary.items()}


def sort_mix_list(mixed_list: list) -> list:
    gen = iter(sorted([item for item in mixed_list if isinstance(item, str)]))
    return [next(gen) if isinstance(item, str) else item for item in mixed_list]
