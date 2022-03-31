import requests
import pprint

token = ''

def make_dir(dir_name):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    """Создает директорию на Я-Диксе"""
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {'path': dir_name}
    response = requests.put(url, headers=headers, params=params, timeout=5)
    return response.status_code

def file_list():
    headers = {
        'Accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    """выдает информацию о директории"""
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {'path': '/'}
    response = requests.get(url, headers=headers, params=params, timeout=5)
    return response.json()

if __name__ == '__main__':
    print(file_list()['_embedded']['items'][0]['name'])
    for i in file_list()['_embedded']['items']:
        print(i['name'])
