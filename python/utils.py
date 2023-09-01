import os

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Globals:
    DEBUG = bool(os.getenv("DEBUG", False))


@dataclass
class DataFiles:
    """
    Intended for retrieving the full file path of both
    decodes.json and encodes.csv for the script to open later
    """

    data_folder = "data"
    decodes_json_file_name = "decodes.json"
    encodes_csv_file_name = "encodes.csv"

    decodes_json_file_path = os.path.join(
        os.path.dirname(__file__), data_folder, decodes_json_file_name
    )
    encodes_csv_file_path = os.path.join(
        os.path.dirname(__file__), data_folder, encodes_csv_file_name
    )


@dataclass
class EncodeFields:
    long_url = "long_url"
    domain = "domain"
    hash = "hash"

    field_names_set = {long_url, domain, hash}


class TimeUtils:
    """
    A utils class intended to properly extract the
    year from each timestamp in decodes.json
    """

    def __init__(self, date_string_format: str = None) -> None:
        self.date_string_format_default = "%Y-%m-%dT%H:%M:%SZ"

        self.date_string_format = (
            self.date_string_format_default
            if date_string_format is None
            else date_string_format
        )

    def transform_date(self, date_string: str) -> datetime:
        date_object = datetime.strptime(date_string, self.date_string_format)
        return date_object

    def get_date_string_year(self, date_string: str) -> int:
        date_object = self.transform_date(date_string)
        return date_object.year
