import requests
import datetime as dt

parameters = {
    "token": 'jdhf87qw6f87sy3445092ugsklj985',
    'username': 'lkariml',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url='https://pixe.la/v1/users', json=parameters)
# print(response.text)

graph_endpoint = f'https://pixe.la/v1/users/lkariml/graphs'

graph_config = {
    'id': 'firstgraph',
    'name': 'Coding Graph',
    'unit': 'h',
    'type': 'float',
    'color': 'kuro'
}
headers = {
    "X-USER-TOKEN": 'jdhf87qw6f87sy3445092ugsklj985'
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = dt.datetime.now()
cell = {
    'date': today.strftime('%y%m%d'),
    'quantity': "2.0",
    'oprionalData': "test"
}

response = requests.post(url='https://pixe.la/v1/users/lkariml/graphs/firstgraph', json=cell, headers=headers)
print(response.text)