import unittest

from datetime import datetime

from utils import TimeUtils


class TestTimeUtils(unittest.TestCase):
    valid_date_string = "2021-01-01T00:00:00Z"
    invalid_date_string = "foo"

    def test_passing_in_timestamp_format_overrides_default(self) -> None:
        new_date_string_format = "foo-bar"
        time_utils = TimeUtils(new_date_string_format)
        self.assertEqual(new_date_string_format, time_utils.date_string_format)

    def test_date_string_format_set_to_default_when_no_format_passed_as_parameter(
        self,
    ) -> None:
        time_utils = TimeUtils()
        self.assertEqual(
            time_utils.date_string_format, time_utils.date_string_format_default
        )

    def test_passing_valid_date_string_to_transform_date_returns_datetime_object(
        self,
    ) -> None:
        time_utils = TimeUtils()

        try:
            datetime_object = time_utils.transform_date(self.valid_date_string)
            self.assertIsInstance(datetime_object, datetime)
        except:
            assert False

    def test_passing_invalid_date_string_to_transform_date_throws_value_error(
        self,
    ) -> None:
        time_utils = TimeUtils()

        try:
            time_utils.transform_date(self.invalid_date_string)
        except ValueError:
            return
        assert False

    def test_passing_valid_date_string_to_get_date_string_year_returns_datetime_object(
        self,
    ) -> None:
        time_utils = TimeUtils()

        try:
            year_value = time_utils.get_date_string_year(self.valid_date_string)
            self.assertIsInstance(year_value, int)
        except:
            assert False

    def test_passing_invalid_date_string_to_get_date_string_year_throws_value_error(
        self,
    ) -> None:
        time_utils = TimeUtils()

        try:
            time_utils.get_date_string_year(self.invalid_date_string)
        except ValueError:
            return
        assert False

    @staticmethod
    def run_tests() -> None:
        unittest.main()
