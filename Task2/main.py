import configparser
import requests


def create_folder(token):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {token}'}
    params = {'path': 'folder/'}
    return requests.put(url, headers=headers, params=params)


def authorization():
    config = configparser.ConfigParser()
    config.read('token.ini')
    access = config['Yandex']['yandex']
    return access

def delete_folder():
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
               'Authorization': f'OAuth {authorization()}'}
    params = {'path': 'folder/'}
    return requests.delete(url, headers=headers, params=params)


if '__main__' == __name__:
    print(create_folder(authorization()).status_code)