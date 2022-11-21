import os
import task

def test_get_info_hrefs():
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

    os.remove('task.json')
    assert task.get_info_hrefs(args_control2) and os.path.exists('task.json')

    os.remove('task.json')
    assert task.get_info_hrefs('hello') == ({})  and os.path.exists('task.json')

    os.remove('task.json')
    assert task.get_info_hrefs(None) == ({})  and os.path.exists('task.json')

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

    os.remove('task.json')
    assert task.get_info_hrefs(args_control) == result_control and os.path.exists('task.json')