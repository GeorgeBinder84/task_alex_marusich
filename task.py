import json
import requests
import re
def get_https_methods(array_urls):
    methods = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS', 'CONNECT', 'TRACE']
    def run_http_methods(str_url, str_method):

        try:
            session = requests.Session()
            ref_method = getattr(session, str_method.lower())
            status = ref_method(str_url).status_code
            return status
        except (requests.exceptions.RequestException):
            return 405
        except AttributeError:
            return 405

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

    def  delete_items_there_are_not_urls(arr):
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

    def main():
        for i_url in array_urls:
            for i_method in methods:
                results[i_url][i_method] = run_http_methods(i_url, i_method)


    array_urls = create_set(array_urls)
    array_urls = delete_items_there_are_not_urls(array_urls)
    results = create_structure(array_urls)
    main()
    results = clean_structure(results)
    create_and_write_to_file(results)
    return results

# time taken: 13.663326116045937
'''
if __name__ == '__main__':
    args_control = {    "1",
                        "https://google.com",
                        "https://www.facebook.com"
                    }
    print(get_https_methods(args_control))
'''