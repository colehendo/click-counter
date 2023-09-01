import unittest

from bitly_urls import BitlyURLs
from click_counter import ClickCountValidator
from utils import TimeUtils


class TestClickCountValidator(unittest.TestCase):
    bitly_urls = BitlyURLs()

    year = 2021

    valid_short_urls = bitly_urls.valid_short_urls
    valid_url = list(valid_short_urls)[0]
    valid_date = "2021-01-01T00:00:00Z"

    invalid_url = "foo"
    invalid_date = "foo"

    def test_initializing_class_initializes_time_utils_class(self) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        self.assertIsInstance(click_count_validator.time_utils, TimeUtils)

    def test_passing_list_including_null_value_to_required_fields_have_data_returns_false(
        self,
    ) -> None:
        null_required_fields = [None]
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        required_fields_have_data = click_count_validator.required_fields_have_data(
            null_required_fields
        )

        self.assertFalse(required_fields_have_data)

    def test_passing_list_of_strings_to_required_fields_have_data_returns_true(
        self,
    ) -> None:
        null_required_fields = ["foo"]
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        required_fields_have_data = click_count_validator.required_fields_have_data(
            null_required_fields
        )

        self.assertTrue(required_fields_have_data)

    def test_passing_empty_list_to_required_fields_have_data_returns_true(self) -> None:
        null_required_fields = []
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        required_fields_have_data = click_count_validator.required_fields_have_data(
            null_required_fields
        )

        self.assertTrue(required_fields_have_data)

    def test_passing_invalid_date_to_click_meets_conditions_returns_false(self) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_meets_conditions = click_count_validator.click_meets_conditions(
            self.valid_url, self.invalid_date
        )

        self.assertFalse(click_meets_conditions)

    def test_passing_date_not_in_2021_to_click_meets_conditions_returns_false(
        self,
    ) -> None:
        date_not_in_2021 = "2022-01-01T00:00:00Z"
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_meets_conditions = click_count_validator.click_meets_conditions(
            self.valid_url, date_not_in_2021
        )

        self.assertFalse(click_meets_conditions)

    def test_passing_invalid_url_to_click_meets_conditions_returns_false(self) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_meets_conditions = click_count_validator.click_meets_conditions(
            self.invalid_url, self.valid_date
        )

        self.assertFalse(click_meets_conditions)

    def test_passing_valid_url_and_valid_date_to_click_meets_conditions_returns_true(
        self,
    ) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_meets_conditions = click_count_validator.click_meets_conditions(
            self.valid_url, self.valid_date
        )

        self.assertTrue(click_meets_conditions)

    def test_passing_null_parameters_to_click_is_valid_returns_false(self) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_is_valid = click_count_validator.click_is_valid(None, None)

        self.assertFalse(click_is_valid)

    def test_passing_invalid_url_to_click_is_valid_returns_false(self) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_is_valid = click_count_validator.click_is_valid(
            self.invalid_url, self.valid_date
        )

        self.assertFalse(click_is_valid)

    def test_passing_invalid_date_to_click_is_valid_returns_false(self) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_is_valid = click_count_validator.click_is_valid(
            self.valid_url, self.invalid_date
        )

        self.assertFalse(click_is_valid)

    def test_passing_valid_url_and_valid_date_to_click_is_valid_returns_true(
        self,
    ) -> None:
        click_count_validator = ClickCountValidator(self.valid_short_urls, self.year)
        click_is_valid = click_count_validator.click_is_valid(
            self.valid_url, self.valid_date
        )

        self.assertTrue(click_is_valid)

    @staticmethod
    def run_tests() -> None:
        unittest.main()
