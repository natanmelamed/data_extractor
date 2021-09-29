import pytest

from common_utils import load_data_from_json_file, sort_dict_by_keys
from data_extractor import DataExtractor


class TestDataExtractorTests:
    @pytest.mark.data_extractor
    def test_data_processor(self) -> None:
        DataExtractor(path="python exercise.json").data_processor()
        actual_result = load_data_from_json_file(file_path="expected_processed_data.json")
        expected_result = load_data_from_json_file(file_path="processed_data.json")
        actual_result = sort_dict_by_keys(actual_result)
        expected_result = sort_dict_by_keys(expected_result)
        assert actual_result == expected_result
