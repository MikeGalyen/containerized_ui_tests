import sys

sys.path.append('../..')

from app.api_tools.api_data import APIData
from app.api_tools.api_calls import APICalls
import pytest

data = APIData()
api_helper = APICalls()


def test_get_token():
    status_code, token_data = api_helper.get_token(data.auth_url, data.auth_data)
    assert status_code == 200, f"Status code, {status_code} received when, 200 was expected"
