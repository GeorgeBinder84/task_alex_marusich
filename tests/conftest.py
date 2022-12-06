import pytest
import requests
from time import perf_counter

import os

@pytest.fixture(scope="session")
def get_sync_session():
    session = requests.Session()
    return session

from src.enums.task_enums import BIG_ZUCKERBERG
@pytest.fixture(params=[BIG_ZUCKERBERG,])
def get_url(request):
    yield request.param

from src.enums.task_enums import HTTPS_METHODS
@pytest.fixture(params=HTTPS_METHODS)
def get_https_method(request):
    yield request.param



@pytest.fixture
def preparation_and_cleanring():
    try:
        os.remove('task.json')
    except:
        pass
    start = perf_counter()
    yield
    stop = perf_counter()
    print("time taken:", stop - start)
    assert os.path.exists('task.json')


from src.enums.task_enums import dict_url_for_validate
@pytest.fixture(scope="module", params=dict_url_for_validate.items())
def get_urlstring_for_validate(request):
    yield {'url': request.param[0], 'validate': request.param[1]}

