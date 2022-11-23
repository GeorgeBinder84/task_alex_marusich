import os
import task
from time import perf_counter
def test_get_info_hrefs():
    start = perf_counter()
    args_control2 = [    '1',
                    'w3.com',
                    'http://w3.com',
                    'www.w3.com',
                    'www.linkedin.com',
                    'https://www.linkedin.com',
                    'www.linkedin.com/in/george-binder',
                    'www.google.com',
                    'https://www.google.com',
                    'https://www.linkedin.com/in/george-binder/',
                    'https://pythonexamples.org/',
                    'www.linkedin.com',
                    'https://www.linkedin.com',
                    'www.linkedin.com/in/george-binder',
                    'www.google.com',
                    'linkedin.com/in/george-binder/',
                    'pythonexamples.org/',]
    try:
        os.remove('task.json')
    except:
        pass
    assert task.get_https_methods(args_control2)
    assert os.path.exists('task.json')

    stop = perf_counter()
    print("time taken:", stop - start)

    try:
        os.remove('task.json')
    except:
        pass
    assert task.get_https_methods('hello') == {}
    assert os.path.exists('task.json')

    try:
        os.remove('task.json')
    except:
        pass
    assert task.get_https_methods(None) == {}
    assert os.path.exists('task.json')

    args_control = {    "1",
                        "https://google.com",
                        "https://www.facebook.com"}

    result_control = {
        'https://google.com': {'GET': 200,
                               'HEAD': 301},
         'https://www.facebook.com': {'DELETE': 200,
                                      'GET': 200,
                                      'HEAD': 200,
                                      'OPTIONS': 200,
                                      'PATCH': 200,
                                      'POST': 200,
                                      'PUT': 200}}

    try:
        os.remove('task.json')
    except:
        pass
    assert task.get_https_methods(args_control) == result_control
    assert os.path.exists('task.json')
    print("time taken:", stop - start)
#18.10932699299883