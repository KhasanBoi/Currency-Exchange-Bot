import requests
import settings

url = settings.URL
response = requests.get(url)
data = response.json()
y = data["conversion_rates"]['UZS']