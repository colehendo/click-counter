from tests.urls_tests import TestURLs
from tests.click_count_logger_tests import TestClickCountLogger
from tests.click_counter_tests import TestClickCounter
from tests.click_count_validator_tests import TestClickCountValidator
from tests.time_utils_tests import TestTimeUtils


def run_all_tests() -> None:
    TestURLs().run_tests()
    TestClickCountLogger().run_tests()
    TestClickCounter().run_tests()
    TestClickCountValidator().run_tests()
    TestTimeUtils().run_tests()


if __name__ == "__main__":
    run_all_tests()
