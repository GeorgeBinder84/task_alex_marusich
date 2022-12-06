# task_alex_marusich
Тестовое задание от Алексея Марусича.
Времени затрачено 4 дня, но первоначальное решене было сделано за 2 часа. Большая часть времени потрачена на requests, poetry, deploy, pytest, coverage

Name           Stmts   Miss  Cover   Missing
--------------------------------------------
task.py           37      2    95%   59-60
test_task.py      14      0   100%
--------------------------------------------
TOTAL             51      2    96%




Исправил замечания(те, что успел понять):
Разбил процедуры на отдельные процедуры.
Переименовал функцию 'get_info_hrefs' в 'get_https_methods'
Заменил pytest на aiohttp - ускорил 'get_https_methods' работу в несколько раз
Использовал фикстуры(на столько, на сколько понял)
Отладил функцию на src/enums/task/enums.py

(venv) binder@V110:~/PycharmProjects/test_alex_marusich/tests$ coverage run -m pytest -v -s
============================================================================================================================================= test session starts =============================================================================================================================================
platform linux -- Python 3.8.10, pytest-7.2.0, pluggy-1.0.0 -- /home/binder/PycharmProjects/test_alex_marusich/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/binder/PycharmProjects/test_alex_marusich/tests
plugins: asyncio-0.20.2, aiohttp-1.0.4
asyncio: mode=strict
collected 37 items

test_task.py::test_mpv PASSED
test_task.py::test_full_speed Строка '' не является ссылкой.
Строка 'www.w3.com' не является ссылкой.
Строка 'htps://' не является ссылкой.
Строка ' https://www.google.com' не является ссылкой.
Строка 'pythonexamples.org/' не является ссылкой.
Строка 'htps://www.google.com' не является ссылкой.
Строка 'www.linkedin.com' не является ссылкой.
Строка '1' не является ссылкой.
Строка 'w3.com' не является ссылкой.
Строка 'www.google.com' не является ссылкой.
Строка 'www.linkedin.com/in/george-binder' не является ссылкой.
Строка 'https:/www.google.com' не является ссылкой.
Строка 'https://' не является ссылкой.
Строка 'linkedin.com/in/george-binder/' не является ссылкой.
{'https://www.google.com': {'GET': 200, 'HEAD': 200}, 'https://ww.google.com': {'GET': 200, 'POST': 200, 'HEAD': 302}, 'https://www.linkedin.com/in/george-binder/': {'GET': 999, 'POST': 999, 'PUT': 999, 'HEAD': 999, 'DELETE': 999, 'PATCH': 403, 'OPTIONS': 999}, 'https://www.linkedin.com': {'GET': 200, 'POST': 403, 'PUT': 403, 'HEAD': 200, 'DELETE': 403, 'PATCH': 403, 'OPTIONS': 404}, 'http://www.google.com': {'GET': 200, 'HEAD': 200}, 'https://pythonexamples.org/': {'GET': 200, 'POST': 200, 'PUT': 200, 'HEAD': 200, 'DELETE': 200, 'PATCH': 200, 'OPTIONS': 200}, 'http://w3.com': {'GET': 200, 'POST': 403, 'PUT': 403, 'HEAD': 301, 'DELETE': 403, 'PATCH': 403, 'OPTIONS': 403}, 'http://обирай.укр': {'GET': 200, 'POST': 200, 'HEAD': 200}, 'http://wwwgoogle.com': {'GET': 200, 'POST': 200, 'HEAD': 301}}
PASSED
test_task.py::test_sync_connection[https://www.facebook.com-GET] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-POST] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-PUT] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-HEAD] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-DELETE] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-PATCH] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-OPTIONS] PASSED
test_task.py::test_sync_connection[https://www.facebook.com-CONNECT] FAILED
test_task.py::test_sync_connection[https://www.facebook.com-TRACE] FAILED
test_task.py::test_check_string_is_url[https://www.google.com] PASSED
test_task.py::test_check_string_is_url[http://www.google.com] PASSED
test_task.py::test_check_string_is_url[http://\u043e\u0431\u0438\u0440\u0430\u0439.\u0443\u043a\u0440] PASSED
test_task.py::test_check_string_is_url[https://nonexistentwebsite.com] PASSED
test_task.py::test_check_string_is_url[https://www.linkedin.com/in/george-binder/] PASSED
test_task.py::test_check_string_is_url[https://pythonexamples.org/] PASSED
test_task.py::test_check_string_is_url[https://www.linkedin.com] PASSED
test_task.py::test_check_string_is_url[http://wwwgoogle.com] PASSED
test_task.py::test_check_string_is_url[https://www.googlecom] PASSED
test_task.py::test_check_string_is_url[http://w3.com] PASSED
test_task.py::test_check_string_is_url[ https://www.google.com] Строка ' https://www.google.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[https://] Строка 'https://' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[htps://] Строка 'htps://' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[www.google.com] Строка 'www.google.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[https:/www.google.com] Строка 'https:/www.google.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[htps://www.google.com] Строка 'htps://www.google.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[https://ww.google.com] PASSED
test_task.py::test_check_string_is_url[] Строка '' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[1] Строка '1' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[w3.com] Строка 'w3.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[www.w3.com] Строка 'www.w3.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[www.linkedin.com] Строка 'www.linkedin.com' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[www.linkedin.com/in/george-binder] Строка 'www.linkedin.com/in/george-binder' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[linkedin.com/in/george-binder/] Строка 'linkedin.com/in/george-binder/' не является ссылкой.
PASSED
test_task.py::test_check_string_is_url[pythonexamples.org/] Строка 'pythonexamples.org/' не является ссылкой.
PASSED
test_task.py::test_create_arg_set PASSED

================================================================================================================================================== FAILURES ===================================================================================================================================================
___________________________________________________________________________________________________________________________ test_sync_connection[https://www.facebook.com-CONNECT] ____________________________________________________________________________________________________________________________

get_sync_session = <requests.sessions.Session object at 0x7f8402b3b280>, get_url = 'https://www.facebook.com', get_https_method = 'CONNECT'

    def test_sync_connection(get_sync_session, get_url, get_https_method):
>       status = getattr(get_sync_session, get_https_method.lower())(get_url).status_code
E       AttributeError: 'Session' object has no attribute 'connect'

test_task.py:12: AttributeError
____________________________________________________________________________________________________________________________ test_sync_connection[https://www.facebook.com-TRACE] _____________________________________________________________________________________________________________________________

get_sync_session = <requests.sessions.Session object at 0x7f8402b3b280>, get_url = 'https://www.facebook.com', get_https_method = 'TRACE'

    def test_sync_connection(get_sync_session, get_url, get_https_method):
>       status = getattr(get_sync_session, get_https_method.lower())(get_url).status_code
E       AttributeError: 'Session' object has no attribute 'trace'

test_task.py:12: AttributeError
=========================================================================================================================================== short test summary info ===========================================================================================================================================
FAILED test_task.py::test_sync_connection[https://www.facebook.com-CONNECT] - AttributeError: 'Session' object has no attribute 'connect'
FAILED test_task.py::test_sync_connection[https://www.facebook.com-TRACE] - AttributeError: 'Session' object has no attribute 'trace'
======================================================================================================================================== 2 failed, 35 passed in 10.46s ========================================================================================================================================
(venv) binder@V110:~/PycharmProjects/test_alex_marusich/tests$ coverage report
Name                                                                      Stmts   Miss  Cover
---------------------------------------------------------------------------------------------
/home/binder/PycharmProjects/test_alex_marusich/src/enums/__init__.py         0      0   100%
/home/binder/PycharmProjects/test_alex_marusich/src/enums/task_enums.py       7      0   100%
/home/binder/PycharmProjects/test_alex_marusich/task.py                      68      1    99%
__init__.py                                                                   0      0   100%
conftest.py                                                                  42      9    79%
test_task.py                                                                 20      0   100%
---------------------------------------------------------------------------------------------
TOTAL                                                                       137     10    93%
(venv) binder@V110:~/PycharmProjects/test_alex_marusich/tests$
