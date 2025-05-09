from api.solana_api import fetch_solana_performance
import json

#recupoerer les objets

samples = fetch_solana_performance()
data = [json.loads(sample.to_json()) for sample in samples]
print(json.dumps(data, indent=2))