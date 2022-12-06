import task
import src.enums.task_enums as data_tests
from time import perf_counter

def test_mpv(preparation_and_cleanring):
    assert data_tests.result_1 == task.get_https_methods(data_tests.arg_1)
def test_full_speed(preparation_and_cleanring, get_set_urls):
    result = task.get_https_methods(get_set_urls)
    print(result)

def test_sync_connection(get_sync_session, get_url, get_https_method):
    status = getattr(get_sync_session, get_https_method.lower())(get_url).status_code
    assert 405 != status

def test_check_string_is_url(get_urlstring_for_validate):
    url = get_urlstring_for_validate
    assert_value = data_tests.dict_url_for_validate[url]
    assert assert_value == task._check_is_url(url)

def test_create_arg_set():
    for i in data_tests.set_args2.keys():
        arg     = data_tests.set_args2[i]
        assert_result  = data_tests.set_results2[i]
        assert  assert_result == task._create_arg_set(arg)


