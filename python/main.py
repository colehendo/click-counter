from bitly_urls import BitlyURLs
from click_counter import ClickCounter, ClickCountLogger
from args import ParseArguments
from typing import List, Dict


def main() -> List[Dict[str, int]]:
    args = ParseArguments().parse()
    bitly_urls = BitlyURLs(encodes_file_path=args.encodes_file_path)
    click_counter = ClickCounter(bitly_urls.valid_short_urls, decodes_file_path=args.decodes_file_path)
    click_counter.count_clicks()
    logger = ClickCountLogger(
        short_to_long_url_map=bitly_urls.url_map,
        click_count_per_short_url=click_counter.click_count_per_url,
    )

    result = logger.map_short_url_count_to_long_url_count()
    return result
    # logger.output_long_urls_and_clicks()


if __name__ == "__main__":
    main()
