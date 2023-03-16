from argparse import Namespace, ArgumentParser
from flask_restful import Api, Resource, reqparse


class ParseArguments:
    @staticmethod
    def parse() -> Namespace:
        parser = reqparse.RequestParser()

        parser.add_argument(
            "--encodes-file-path",
            type=str,
            help="Path to the encodes JSON file",
            default="/Users/colehendo/Desktop/bitly-backend-eng-coding-challenge/src/data/encodes.csv",
        )
        parser.add_argument(
            "--decodes-file-path",
            type=str,
            help="Path to the decodes JSON file",
            default="data/decodes.json",
        )
        parser.add_argument("--year")

        return parser.parse_args()
