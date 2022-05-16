
from random import random
import threading
import requests
import urllib
import random
proxies = open('proxy.txt', 'r').read().splitlines()
proxies = [{'http': 'http://' + proxy} for proxy in proxies]


def post(id, normalid):

    try:
        params = {
            'id': normalid,  # ,normalid normalid
            'ranking_id': id
        }
        params = urllib.parse.urlencode(params)
        momo = requests.post("https://rancolle.com/vote.php",
                             headers={"Content-Type": 'application/x-www-form-urlencoded', 'Origin': 'https://rancolle.com', 'Referer': f'https://rancolle.com/ranking.php?id={str(id)}', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'Upgrade-Insecure-Requests': "1", 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}, data=params, proxies=random.choice(proxies))
        print(str(momo.reason))
    except Exception as e:
        print("Error :" + str(e))


if __name__ == '__main__':
    ranking_id = input("ranking ID: ")
    normal_id = input("Noramal ID: ")
    for _ in range(5):
        threading.Thread(target=post, args=(ranking_id, normal_id)).start()
