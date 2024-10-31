# Ex12_1.py

import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        print("Here's a Chuck Norris joke for you:")
        print(data["value"])  # Print only the joke text
    except requests.exceptions.RequestException as e:
        print("Error fetching joke:", e)

if __name__ == "__main__":
    get_chuck_norris_joke()
