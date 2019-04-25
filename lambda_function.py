# -*- coding: utf-8 -*-
# pylint: disable=invalid-name,too-few-public-methods
"""
Lambda tutorial script for Python3
"""

import json
import requests

def main():

    URL = "IncommingWebhooksURL"

    contents = {
        "text": ":telephone_receiver: :open_mouth: もしもし",
        "username": "nakashun",
        "channel": "#channel",
    }

    r = requests.post(URL, data=json.dumps(contents))

    pass

def lambda_handler(event, context):
    main()
    pass

if __name__ == "__main__":
    main()
    pass
