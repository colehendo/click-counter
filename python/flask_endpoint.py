from bitly_urls import BitlyURLs
from click_counter import ClickCounter, ClickCountLogger
from args import ParseArguments
from typing import List, Dict
from flask import Flask, request

# from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
# api = Api(app)


@app.route("/clicks", methods=["GET"])
def clicks():
    args = request.args
    args_dict = args.to_dict()

    bitly_urls = BitlyURLs()
    # click_counter = ClickCounter(
    #     bitly_urls.valid_short_urls, year=2021
    # )
    click_counter = ClickCounter(
        bitly_urls.valid_short_urls, year=args_dict.get("year", 2021)
    )
    click_counter.count_clicks()
    logger = ClickCountLogger(
        short_to_long_url_map=bitly_urls.url_map,
        click_count_per_short_url=click_counter.click_count_per_url,
    )

    result = logger.map_short_url_count_to_long_url_count()
    return result


# class Clicks(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()  # initialize

#         parser.add_argument("year", required=True)

#         args = parser.parse_args()  # parse arguments to dictionary
#         bitly_urls = BitlyURLs()
#         # click_counter = ClickCounter(
#         #     bitly_urls.valid_short_urls, year=2021
#         # )
#         click_counter = ClickCounter(bitly_urls.valid_short_urls, year=args["year"])
#         click_counter.count_clicks()
#         logger = ClickCountLogger(
#             short_to_long_url_map=bitly_urls.url_map,
#             click_count_per_short_url=click_counter.click_count_per_url,
#         )

#         result = logger.map_short_url_count_to_long_url_count()
#         print("got result")
#         print(result)
#         return {"data": result}, 200


# def create_endpoints():
# api.add_resource(Clicks, "/clicks")


if __name__ == "__main__":
    app.run()
