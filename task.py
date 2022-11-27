import json
import aiohttp
import re
import asyncio

def get_https_methods(array_urls):
    methods = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS', 'CONNECT', 'TRACE']
    async def get_response_status(obj_session, str_url, str_https_method):
        try:
            async with getattr(obj_session, str_https_method.lower())(str_url) as response:
                return {'url': str_url, 'https_method': str_https_method, 'response_status': response.status}
        except (aiohttp.ClientResponseError, AttributeError):
            return {'url': str_url, 'https_method': str_https_method, 'response_status': 405}

    URL_REGEX = re.compile(r"^(?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")
    def check_is_url(str_url):
        if type(str_url) == str and  re.match(URL_REGEX, str_url):
            return True
        else:
            print(f"Строка '{str_url}' не является ссылкой.")
            return False

    def create_set(arr):
        if hasattr(arr, '__iter__') and type(arr) != str:
            arr = set(arr)
        else:
            arr = {arr,}
        return arr

    def  delete_items_there_are_not_urls(arr): #!
        result = list()
        for item in arr:
            if check_is_url(item) == True:
                result.append(item)
        return set(result)

    def create_structure(array_urls):
        result = {}
        for url in array_urls:
            result[url] = {}
            for method in methods:
                result[url][method] = 405
        return result

    def clean_structure(array_urls):
        for url in array_urls:
            for method in methods:
                if array_urls[url][method] == 405:
                    del array_urls[url][method]
            if array_urls[url] == {}:
                del array_urls[url]

        return array_urls

    def  create_and_write_to_file(arr):
        with open("task.json", "w") as outfile:
            json.dump(arr, outfile)

    async def main(array_urls, out_set_results):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i_url in array_urls:
                for i_method in methods:
                    task = asyncio.create_task(get_response_status(session, i_url, i_method))
                    tasks.append(task)
                results = await asyncio.gather(*tasks)
                for r in results:
                    out_set_results[r['url']][r['https_method']] = r['response_status']
        return out_set_results

    array_urls = create_set(array_urls)
    array_urls = delete_items_there_are_not_urls(array_urls)
    results = create_structure(array_urls)
    results = asyncio.run(main(array_urls, results))
    results = clean_structure(results)
    create_and_write_to_file(results)
    return results

# time taken: 13.663326116045937

if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()

    args_control = {    "1",
                        "https://google.com",
                        "https://www.facebook.com"
                    }
    print(get_https_methods(args_control))

    stop = perf_counter()
    print("time taken:", stop - start)
# time taken: 3.5 - 4.5
# time taken: 0.7694479780038819