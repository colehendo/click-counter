import csv

from functools import cached_property
from typing import Dict, List

from utils import DataFiles, EncodeFields, Globals


class URLs:
    """
    Reads in the encodes.csv file and
    stores the data in an ingestable manner
    """

    _url_map = None
    url_base = "http://"

    @cached_property
    def url_map(self) -> Dict[str, str]:
        """"""
        if self._url_map is None:
            self.set_url_map()

        return self._url_map

    @cached_property
    def valid_short_urls(self) -> List[str]:
        return list(self.url_map.keys())

    def validate_encode_field_names(self, encode_entry: Dict[str, str]) -> None:
        """Ensures the field names in encodes.csv match what is expected"""
        encode_entry_field_names = encode_entry.keys()
        if EncodeFields.field_names_set != set(encode_entry_field_names):
            raise ValueError(
                f"Field names in {DataFiles.encodes_csv_file_name} should be {str(EncodeFields.field_names_set)} but were {str(encode_entry_field_names)}"
            )

    def add_remainder_urls_to_map(self, encode_entry: Dict[str, str]) -> None:
        short_url = f"{self.url_base}{encode_entry[EncodeFields.domain]}/{encode_entry[EncodeFields.hash]}"
        self.url_map[short_url] = encode_entry[EncodeFields.long_url]

    def add_url_to_map(self, encode_entry: Dict[str, str]) -> None:
        """
        Since all encode entries have the same fields,
        the field names only need to be validated once.

        This function validates those field names once
        and then sets itself to the function which maps those fields to a url.

        By doing this, it eliminates the need either for
        a conditional statement per loop checking if it is the first entry,
        or a validation check per loop.
        """

        self.validate_encode_field_names(encode_entry)
        self.add_remainder_urls_to_map(encode_entry)
        self.add_url_to_map = self.add_remainder_urls_to_map

    def set_url_map(self) -> None:
        """
        This function reads the encodes.csv file into a dict
        to ensure the right fields are being consumed in the right order
        and builds a short to long url map from the data
        """

        self._url_map = {}

        with open(DataFiles.encodes_csv_file_path) as encodes_file:
            encodes_reader = csv.DictReader(encodes_file)
            for encode_entry in encodes_reader:
                if not isinstance(encode_entry, dict):
                    if Globals.DEBUG:
                        print(
                            f"The following encode entry was not a dict: {str(encode_entry)}"
                        )
                    continue

                self.add_url_to_map(encode_entry)
