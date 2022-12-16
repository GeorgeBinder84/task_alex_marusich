import json
import aiohttp
import re
import asyncio
import copy

METHODS = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS', 'CONNECT', 'TRACE']
URL_REGEX = re.compile(r'^(?:http(s)?:\/\/)\S+')
async def _get_response_status(obj_session, str_url, str_https_method):
    try:
        async with getattr(obj_session, str_https_method.lower())(str_url) as response:
            return {'url': str_url, 'https_method': str_https_method, 'response_status': response.status}
    except (AttributeError, aiohttp.ClientResponseError, aiohttp.ClientConnectorError):
        return {'url': str_url, 'https_method': str_https_method, 'response_status': 405}


def _check_is_url(str_url):
    if type(str_url) == str and re.match(URL_REGEX, str_url):
        return True
    else:
        print(f"Строка '{str_url}' не является ссылкой.")
        return False


def _create_arg_set(arr):
    if hasattr(arr, '__iter__') and type(arr) != str:
        arr = set(map(str,arr))
    else:
        arr = {str(arr)}
    return arr


def _delete_items_there_are_not_urls(arr):  # !
    result = list()
    for item in arr:
        if _check_is_url(item) == True:
            result.append(item)
    return set(result)


def _create_structure(array_urls):
    result = {}
    for url in array_urls:
        result[url] = {}
        for method in METHODS:
            result[url][method] = 405
    return result


def _clean_structure(array_urls):
    for url in array_urls.copy():
        for method in METHODS:
            if not array_urls[url]:
                array_urls.pop(url)
            if array_urls[url][method] == 405:
                del array_urls[url][method]
        if array_urls[url] == {}:
            del array_urls[url]
    return array_urls


def _create_and_write_to_file(arr):
    with open("task.json", "w") as outfile:
        json.dump(arr, outfile)


async def _main(array_urls, out_set_results):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i_url in array_urls:
            for i_method in METHODS:
                task = asyncio.create_task(_get_response_status(session, i_url, i_method))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            for r in results:
                out_set_results[r['url']][r['https_method']] = r['response_status']
    return out_set_results


def get_https_methods(urls):
    array_urls = _create_arg_set(urls)
    array_urls = _delete_items_there_are_not_urls(array_urls)
    results = _create_structure(array_urls)
    results = asyncio.run(_main(array_urls, results))
    results = _clean_structure(results)
    _create_and_write_to_file(results)
    return results

if __name__ == "__main__":
    test_str = [    '1',
                    'www.linkedin.com',
                    'https://www.linkedin.com',
                    'www.linkedin.com/in/george-binder',
                    'https://www.google.com',
                    'https://www.linkedin.com/in/george-binder/',
                    'https://pythonexamples.org/'] #, 'хрень']

    print(get_https_methods(test_str))
