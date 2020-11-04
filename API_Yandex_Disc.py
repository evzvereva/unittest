import requests


def shelf():
    headers = {'Authorization': 'AgAAAABFBuo5AADLW2ICEHUYE0lXjjPQLHTwfBo'}
    q = requests.put('https://cloud-api.yandex.net/v1/disk/resources?path=music', headers=headers)
    return q.status_code
