BIG_ZUCKERBERG = 'https://www.facebook.com'
HTTPS_METHODS = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS', 'CONNECT', 'TRACE']


arg_1 = {   "https://google.com",
            "https://www.facebook.com"}

result_1 = {
    'https://google.com': {'GET': 200,
                           'HEAD': 301},
    'https://www.facebook.com': {'DELETE': 200,
                                 'GET': 200,
                                 'HEAD': 200,
                                 'OPTIONS': 200,
                                 'PATCH': 200,
                                 'POST': 200,
                                 'PUT': 200}}

set_args2 = {1:1,
             2:'2',
             3: {3,4},
             4: 'Vasa',
             5: ['Petya', 'Petya'],
             6: None,
             7: [3,{5,6}],
             8: [7,[8,9]],
             }

set_results2 = {1:{'1'},
                2:{'2'},
                3:{'3', '4'},
                4:{'Vasa'},
                5:{'Petya'},
                6:{'None'},
                7:{'3','{5, 6}'},
                8:{'7','[8, 9]'}
                }

dict_url_for_validate ={
    'https://www.google.com': True,
    'http://www.google.com': True,
    "http://обирай.укр": True,
    'https://nonexistentwebsite.com': True,
    'https://www.linkedin.com/in/george-binder/': True,
    'https://pythonexamples.org/': True,
    'https://www.linkedin.com': True,
    'http://wwwgoogle.com': True,
    'https://www.googlecom': True,  #
    'http://w3.com': True,
    ' https://www.google.com': False,
    'https://': False,
    'htps://': False,
    'www.google.com': False,
    'https:/www.google.com': False,
    'htps://www.google.com': False,
    'https://ww.google.com':True,
    '': False,
    '1':False,
    'w3.com': False,
    'www.w3.com': False,
    'www.linkedin.com': False,
    'www.linkedin.com/in/george-binder': False,
    'linkedin.com/in/george-binder/': False,
    'pythonexamples.org/': False
}
