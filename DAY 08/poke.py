import requests
from matplotlib import pyplot as plt

def url_builder(name):
    return f"https://api.pokemontcg.io/v1/cards?name={name}"

def searching_img(data):
    cards = data["cards"]
    return cards[0]["imageUrl"]

def save_img(response2):
    with open("poke.png", "wb") as f:
        for i in response2.iter_content():
            f.write(i)
    
def img_show():
    img = plt.imread("poke.png")
    plt.imshow(img)
    plt.show()



if __name__=="__main__":
    name = input("Enter pokemon name : ")
    url = url_builder(name)

    response = requests.request("GET", url)
    data = response.json()

    img_url = searching_img(data)
    
    response2 = requests.request("GET", img_url)

    save_img(response2)

    img_show()












    # print(dir(response2))
    # print(help(response2))