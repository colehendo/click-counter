from argparse import Namespace, ArgumentParser


class ParseArguments:
    @staticmethod
    def parse() -> Namespace:
        parser = ArgumentParser()

        parser.add_argument("--year", default=2021, type=int)

        return parser.parse_args()
