import task
import src.enums.task_enums as data_tests

def test_full(preparation_and_cleanring):
    assert data_tests.result_1 == task.get_https_methods(data_tests.arg_1)

def test_check_string_is_url(get_urlstring_for_validate):
    url = get_urlstring_for_validate['url']
    assert_value = get_urlstring_for_validate['validate']
    assert assert_value == task._check_is_url(url)

def test_create_arg_set():
    for i in data_tests.set_args2.keys():
        arg     = data_tests.set_args2[i]
        assert_result  = data_tests.set_results2[i]
        assert  assert_result == task._create_arg_set(arg)


