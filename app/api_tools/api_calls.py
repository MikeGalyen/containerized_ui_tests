import requests
import json
import logging

logger = logging.getLogger(__name__)

class APICalls:

    def __init__(self):
        pass

    def get_token(self, url, data):
        try:
            res = requests.post(url, json=data)
            token_data = json.dumps(res.json(), indent=4)
            status_code = res.status_code
            return status_code, token_data
        except Exception as e:
            logger.debug(f"An exception, {e} occurred trying to POST to the URL, {url} with the data: \n{data}")
            print(f"An exception, {e} occurred trying to POST to the URL, {url} with the data: \n{data}")


if __name__ == "__main__":
    pass
