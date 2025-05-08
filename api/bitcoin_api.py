import requests

API_URL = "https://api.blockchair.com/bitcoin/stats"

# Creating a function to retrieve bitcoin specific data

def fetch_bitcoin_stats():
   res = requests.get(API_URL)
   data = res.json().get("data", {})
   return data

# stats = fetch_bitcoin_stats()
# print(stats)