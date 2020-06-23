import requests

url = "https://currencyapi.net/api/v1/rates?key=NXtUyotjncqJie5GKVEjlBi6FYfjgQuQyjjL&base=USD"

response = requests.request("GET", url)


response_data = response.json()

rates = response_data['rates']


print("one USD is equal to : " + str(rates['INR']))