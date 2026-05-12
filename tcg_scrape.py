import requests
import random

#debug import
import pprint

url = "https://api.scryfall.com"

def get_random_card():
    response = requests.get(f"{url}/cards/random")
    if response.status_code == 200:
        card = response.json()
        
        card_img_url = card['image_uris']['normal']
        img_data = requests.get(card_img_url).content
        with open("highlight_card.jpg", "wb") as f:
            f.write(img_data)
        return card
    else:
        print("Error fetching random card:", response.status_code)
        return None
    
def get_sets():
    response = requests.get(f"{url}/sets")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching sets:", response.status_code)
        return None

def get_set(set_code):
    response = requests.get(f"{url}/sets/{set_code}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching set {set_code}:", response.status_code)
        return None

def get_set_cards(set_code):
    response = requests.get(f"{url}/cards/search?q=s%3A{set_code}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching cards for set {set_code}:", response.status_code)
        return None
    
if __name__ == "__main__":
    random_card = get_random_card()
    if random_card:
        print("Random Card Name:", random_card['name'])
    
    sets = get_sets()
    set_names_images = [(s['name'], s['icon_svg_uri']) for s in sets['data']]
    
    
    print("Available Sets:")
    for name, image in set_names_images:
        print("-", name, "Image URL:", image)
        
    card_list = get_card_list()
    if card_list:
        print("Total Cards Found:", card_list['total_cards'])
    

    # if sets:
    #     pprint.pprint(sets)