import pytest
from time import perf_counter
import os

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
