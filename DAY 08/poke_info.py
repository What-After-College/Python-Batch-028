import requests

name = input("Enter the pokemon name : ")
url=f"https://pokeapi.co/api/v2/pokemon/{name}"

response = requests.request("GET", url)

info = response.json()

print(info['abilities'])