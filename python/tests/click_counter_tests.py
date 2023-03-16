import unittest

from collections import defaultdict

from bitly_urls import BitlyURLs
from click_counter import ClickCounter, ClickCountValidator


class TestClickCounter(unittest.TestCase):
    bitly_urls = BitlyURLs()

    valid_short_urls = bitly_urls.valid_short_urls
    url = "foo"

    def test_initializing_class_initializes_click_count_validator_class(self) -> None:
        click_counter = ClickCounter(self.valid_short_urls)
        self.assertIsInstance(click_counter.validator, ClickCountValidator)

    def test_click_count_per_url_is_default_dict(self) -> None:
        click_counter = ClickCounter(self.valid_short_urls)
        self.assertIsInstance(click_counter.click_count_per_url, defaultdict)

    def test_calling_increment_click_count_per_url_on_new_key_sets_it_to_1(
        self,
    ) -> None:
        click_counter = ClickCounter(self.valid_short_urls)
        click_counter.increment_click_count_per_url(self.url)
        self.assertEqual(click_counter.click_count_per_url[self.url], 1)

    def test_calling_increment_click_count_per_url_on_existing_key_increments_it_by_1(
        self,
    ) -> None:
        click_counter = ClickCounter(self.valid_short_urls)
        click_counter.increment_click_count_per_url(self.url)
        click_counter.increment_click_count_per_url(self.url)
        self.assertEqual(click_counter.click_count_per_url[self.url], 2)

    def test_calling_count_clicks_causes_click_count_per_url_to_remain_default_dict(
        self,
    ) -> None:
        click_counter = ClickCounter(self.valid_short_urls)
        click_counter.count_clicks()

        self.assertIsInstance(click_counter.click_count_per_url, defaultdict)

    def test_calling_count_clicks_does_not_throw_file_not_found_error(self) -> None:
        click_counter = ClickCounter(self.valid_short_urls)

        try:
            click_counter.count_clicks()
        except FileNotFoundError:
            assert False

    @staticmethod
    def run_tests() -> None:
        unittest.main()
