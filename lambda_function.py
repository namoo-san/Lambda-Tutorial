# -*- coding: utf-8 -*-
# pylint: disable=invalid-name,too-few-public-methods
"""
Lambda tutorial script for Python3
"""

import requests

URL = 'http://ci.nii.ac.jp/ncid/BB08796640.json'

def main():
    r = requests.get(URL)
    result = r.json()
    print(result)

def lambda_handler(event, context):
    main()
