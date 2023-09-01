import unittest

from urls import URLs
from utils import EncodeFields


class TestURLs(unittest.TestCase):
    valid_encode_entry = {
        EncodeFields.long_url: "foo",
        EncodeFields.domain: "bar",
        EncodeFields.hash: "baz",
    }
    invalid_encode_entry = {"foo": "bar"}

    def test_url_map_is_map(self) -> None:
        urls = URLs()
        self.assertIsInstance(urls.url_map, dict)

    def test_urls_start_with_url_base(self) -> None:
        urls = URLs()
        for url in urls.url_map.keys():
            self.assertTrue(url.startswith(urls.url_base))

    def test_valid_short_urls_returns_list(self) -> None:
        urls = URLs()
        self.assertIsInstance(urls.valid_short_urls, list)

    @staticmethod
    def test_bad_field_names_raises_value_error() -> None:
        urls = URLs()
        invalid_encode_entry = {"foo": "bar"}
        try:
            urls.validate_encode_field_names(invalid_encode_entry)
        except ValueError:
            return
        assert False

    def test_correct_field_names_raises_no_error(self) -> None:
        urls = URLs()

        try:
            urls.validate_encode_field_names(self.valid_encode_entry)
        except:
            assert False

    def test_calling_add_url_to_map_with_invalid_encode_entry_throws_value_error(
        self,
    ) -> None:
        urls = URLs()

        try:
            urls.add_url_to_map(self.invalid_encode_entry)
        except ValueError:
            return
        assert False

    def test_calling_add_url_to_map_with_valid_encode_entry_adds_entry_to_map(
        self,
    ) -> None:
        urls = URLs()

        urls.add_url_to_map(self.valid_encode_entry)
        short_url = f"{urls.url_base}{self.valid_encode_entry[EncodeFields.domain]}/{self.valid_encode_entry[EncodeFields.hash]}"
        self.assertEqual(
            urls.url_map[short_url],
            self.valid_encode_entry[EncodeFields.long_url],
        )

    def test_calling_add_remainder_urls_to_map_with_valid_encode_entry_adds_entry_to_map(
        self,
    ) -> None:
        urls = URLs()

        urls.add_remainder_urls_to_map(self.valid_encode_entry)
        short_url = f"{urls.url_base}{self.valid_encode_entry[EncodeFields.domain]}/{self.valid_encode_entry[EncodeFields.hash]}"
        self.assertEqual(
            urls.url_map[short_url],
            self.valid_encode_entry[EncodeFields.long_url],
        )

    def test_calling_add_url_to_map_with_valid_encode_entry_sets_add_url_to_map_equal_to_add_remainder_urls_to_map(
        self,
    ) -> None:
        urls = URLs()

        urls.add_remainder_urls_to_map(self.valid_encode_entry)
        self.assertEqual(
            urls.add_url_to_map, urls.add_remainder_urls_to_map
        )

    def test_calling_set_url_map_sets_url_map(self) -> None:
        urls = URLs()
        urls.set_url_map()
        self.assertIsInstance(urls.url_map, dict)

    def test_calling_set_url_map_does_not_throw_file_not_found_error(self) -> None:
        urls = URLs()
        try:
            urls.set_url_map()
        except FileNotFoundError:
            assert False

    @staticmethod
    def run_tests() -> None:
        unittest.main()
