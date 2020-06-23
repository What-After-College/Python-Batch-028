import requests

url = "https://sv443.net/jokeapi/v2/joke/Programming,Miscellaneous?blacklistFlags=racist"

response = requests.request("GET", url)

print(response.text)

