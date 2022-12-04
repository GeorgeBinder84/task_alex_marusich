import task
import src.enums.task_enums as args_and_results
def test_full(preparation_and_cleanring):
    assert args_and_results.result_1 == task.get_https_methods(args_and_results.arg_1)

