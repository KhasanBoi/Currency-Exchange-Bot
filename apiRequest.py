import requests

url = 'https://v6.exchangerate-api.com/v6/a9bacf51ad20839f4bf9adda/latest/USD'
response = requests.get(url)
data = response.json()
y = data["conversion_rates"]['UZS']