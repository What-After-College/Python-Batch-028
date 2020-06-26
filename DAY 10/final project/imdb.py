import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

def get_ids(num=5):
    df = pd.read_csv('links.csv')
    movie_ids = list(df.imdbId)
    start_index = 0
    end_index = num
    return movie_ids[start_index : end_index]

def scrap(id):
    url = "https://www.imdb.com/title/tt{}/".format(str(id).zfill(7))
    response = requests.request("GET", url)
    soup = BeautifulSoup(response.text, 'html.parser')
    info = soup.find('script', attrs={"type": "application/ld+json"})
    info = str(info)[str(info).find('{'):-9]
    json_info = json.loads(info)
    movie_info = {
        "name" : json_info['name'],
        "genre" : json_info['genre'],
        "image" : json_info["image"],
        "description" : json_info["description"]
    }
    return movie_info


def movie_info():
    ids = get_ids(10)
    lis = []
    for id in ids:
        movie_inf = scrap(id)
        lis.append(movie_inf)
    return lis


