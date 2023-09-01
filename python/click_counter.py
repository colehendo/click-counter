import json_stream

from collections import defaultdict
from functools import cached_property
from pprint import pprint
from typing import Dict, List, Optional

from utils import DataFiles, Globals, TimeUtils


class ClickCounter:
    def __init__(self, valid_short_urls: List[str], year: str) -> None:
        self.year = int(year)
        self.validator = ClickCountValidator(valid_short_urls, year)
        self._click_count_per_url = defaultdict(lambda: 0)

    @cached_property
    def click_count_per_url(self) -> defaultdict:
        return self._click_count_per_url

    def increment_click_count_per_url(self, url: str):
        self._click_count_per_url[url] += 1

    def count_clicks(self) -> None:
        """
        This function loops over each entry in decodes.json.
        If the entry meets the conditions outlined in the instructions
        the associated count to its URL is incremented.

        json_stream.load() allows the JSON object to be streamed one entry at a time
        instead of loaded into memory in its entirety, which is the behavior of json.load().
        This alleviates memory concerns which arise when processing large JSON objects
        """

        with open(DataFiles.decodes_json_file_path) as decodes_file:
            decodes_data = json_stream.load(decodes_file, persistent=False)
            for click in decodes_data:
                url = click.get("bitlink")
                date = click.get("timestamp")

                click_valid = self.validator.click_is_valid(url, date)
                if not click_valid:
                    if Globals.DEBUG:
                        print(f"The following click was not valid: {str(click)}")
                    continue
                else:
                    self.increment_click_count_per_url(url)


class ClickCountValidator:
    """
    The methods in this class ensure that the necessary data is present in each click,
    and that the conditions for a click to be recorded have been met according to the instructions.
    """

    def __init__(self, valid_short_urls: List[str], year: int) -> None:
        self.year = year
        self.valid_short_urls = valid_short_urls
        self.time_utils = TimeUtils()

    def required_fields_have_data(self, required_fields: List[Optional[str]]) -> bool:
        return all(field is not None for field in required_fields)

    def click_meets_conditions(self, url: str, date: str) -> bool:
        try:
            date_year = self.time_utils.get_date_string_year(date)
        except ValueError as e:
            if Globals.DEBUG:
                print(e)
            return False

        if date_year != self.year:
            return False
        if url not in self.valid_short_urls:
            return False

        return True

    def click_is_valid(self, url: Optional[str], date: Optional[str]) -> bool:
        if not self.required_fields_have_data(required_fields=[url, date]):
            return False
        if not self.click_meets_conditions(url, date):
            return False

        return True


class ClickCountLogger:
    def __init__(
        self,
        short_to_long_url_map: Dict[str, str],
        click_count_per_short_url: defaultdict,
    ) -> None:
        self.short_to_long_url_map = short_to_long_url_map
        self.click_count_per_short_url = click_count_per_short_url

    def map_short_url_count_to_long_url_count(self) -> List[Dict[str, int]]:
        """
        This sorts the default dict of short URLs mapped to their associated count by descending count
        then transforms it into a list of dictionaries of long URLs and their associated counts.
        """
        sorted_click_count_per_short_url = sorted(
            self.click_count_per_short_url.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        formatted_long_url_count = [
            {self.short_to_long_url_map[short_url]: click_count}
            for short_url, click_count in sorted_click_count_per_short_url
        ]

        return formatted_long_url_count

    def output_long_urls_and_clicks(self) -> None:
        long_url_count = self.map_short_url_count_to_long_url_count()
        pprint(long_url_count)
