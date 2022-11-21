'''
1) Получает на вход произвольное множество строк.														+
2) Итерируется по этим строкам и определяет, является ли эта строка ссылкой или нет.					+
3) Если эта строка не ссылка, выводится уведомление: Строка "X" не является ссылкой.					+
4) Если является ссылкой, то
	1) Приложение должно определить какие методы доступны по этой ссылки
		1) Проверяются все http методы.																	+/- кроме 'CONNECT','TRACE'
		2) Доступным считается метод, обработка которого завершилась не 405 ошибкой.					+
	3) Передаваемые данные и ошибки от сервера не важны.												+
	4) Выполнив запрос приложение сохраняет код ответа.													+
6) Результатом работы приложением будет словарь, состоящий из ссылок и информации о доступных метода.	+
'''

import json
import requests
import re

def get_info_hrefs(strings):
    if hasattr(strings, '__iter__') and type(strings) != str:
        strings = set(strings)
    else:
        strings = {strings,}

    session = requests.Session()
    result = dict()
    URL_REGEX = re.compile(r"^(?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$")

    for i_string in strings:
        #i_string is not None and
        if re.match(URL_REGEX, str(i_string)) is None:
            print(f"Строка '{i_string}' не является ссылкой.")
            continue
        try:
            result_methonds = dict()
            status = session.get(i_string).status_code
            if status == 405: continue
            result_methonds['GET'] = status

            status = session.post(i_string).status_code
            if status != 405: result_methonds['POST'] = status

            status = session.put(i_string).status_code
            if status != 405: result_methonds['PUT'] = status

            status = session.head(i_string).status_code
            if status != 405: result_methonds['HEAD'] = status

            status = session.delete(i_string).status_code
            if status != 405: result_methonds['DELETE'] = status

            status = session.patch(i_string).status_code
            if status != 405: result_methonds['PATCH'] = status

            status = session.options(i_string).status_code
            if status != 405: result_methonds['OPTIONS'] = status

            result[i_string] = result_methonds

        except (requests.exceptions.RequestException):
            pass

    with open("task.json", "w") as outfile:
        json.dump(result, outfile)
    return result