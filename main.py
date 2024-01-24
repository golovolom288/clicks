import requests
import os
import argparse


from dotenv import load_dotenv


def is_bitlink(token, link):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"
    headers = {
      "Authorization": token
      }
    response = requests.get(bit_url, headers=headers)
    return response.ok


def shorten_link(token, url):
    bit_url = 'https://api-ssl.bitly.com/v4/shorten'
    params = {
        "long_url": url
    }
    headers = {
      "Authorization": token
      }
    response = requests.post(bit_url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()["id"]


def count_clicks(token, link):
    bit_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"
    params = {
        "unit": "month",
        "units": "-1"
    }
    headers = {
        "Authorization": token
    }
    response = requests.get(bit_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["total_clicks"]
    

if __name__ == "__main__":
    load_dotenv()
    bittoken = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="get url")
    long_url = parser.parse_args()
    
    try:
        if is_bitlink(bittoken, long_url.url):
            print("Количество переходов по ссылке битли:", count_clicks(bittoken, long_url.url))
        else:
            bitlink = shorten_link(bittoken, long_url.url)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print("Вы ввели несуществующий ip")
