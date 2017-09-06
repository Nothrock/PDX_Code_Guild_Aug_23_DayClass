import requests

r = requests.get('http://api.icndb.com/jokes/random')

data = r.json()

print('{}'.format(data['value']['joke']))
