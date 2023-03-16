import sys
import unittest

from io import StringIO

from click_counter import ClickCountLogger


class TestClickCountLogger(unittest.TestCase):
    short_to_long_url_map = {"foo": "bar"}
    click_count_per_short_url = {"foo": 0}

    def test_map_short_url_count_to_long_url_count_returns_list_of_dict(self) -> None:
        click_count_logger = ClickCountLogger(
            self.short_to_long_url_map, self.click_count_per_short_url
        )
        map_short_url_count_to_long_url_count = (
            click_count_logger.map_short_url_count_to_long_url_count()
        )

        self.assertIsInstance(map_short_url_count_to_long_url_count, list)

    def test_output_long_urls_and_clicks_writes_to_stdout(self) -> None:
        captured_output = StringIO()
        sys.stdout = captured_output

        click_count_logger = ClickCountLogger(
            self.short_to_long_url_map, self.click_count_per_short_url
        )
        click_count_logger.output_long_urls_and_clicks()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertTrue(output)  # Checks if the output string is empty or not

    @staticmethod
    def run_tests() -> None:
        unittest.main()
