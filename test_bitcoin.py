from api.bitcoin_api import fetch_bitcoin_stats, fetch_bitcoin_price_usd

stats = fetch_bitcoin_stats()
print("Stats Bitcoin:", stats) # devrait contenir ;les blocs ,mempool_transaction etc.
print("Prix BTC (USD):", fetch_bitcoin_price_usd()) 