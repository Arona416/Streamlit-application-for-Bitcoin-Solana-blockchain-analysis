import streamlit as st
from utils.language import get_text
from api.bitcoin_api import fetch_bitcoin_stats, fetch_bitcoin_price_usd

st.title("Bitcoin") #title page 
st.write(get_text("welcome_text"))

# call the API  to get data 
try:
    stats = fetch_bitcoin_stats()
    btc_price = fetch_bitcoin_price_usd()
except Exception as e:
    st.error(f"Erreur lors de la recuperation des donnees Bitcoin: {e}")   
    st.stop() 

# Extraction des metriques importantes depuis stats 
block_count = stats.get("blocks")
mempool_tx = stats.get("mempool_transaction") 
mempool_tps = stats.get("mempool_tps")   

# Explication  des metriques (multilingue)
st.caption(f"- {get_text('block_count')}: Nombre total de blocs mines (blockchain Bitcoin).")
st.caption(f"- {get_text("mempool_tx")}: Nombre de transaction en attente dans le mempool(non confirmees).")
st.caption(f"- {get_text('btc_price')}: Prix actuel du Bitcoin en dollatrs USD")

# Graphique interactif avec Plotly 
import plotly.graph_objects as go 
# Supposons qu'on trace l'evolution du nombre de transaction en mempool sur 10 intervalle de tenps fictif 
mempool_values = [mempool_tx] * 10  # juste un demo 
fig = go.Figure(go.Scatter(x = list(range(10)), y = mempool_values, mode= 'lines+markers'))
fig.update_layout(title="Mempool Transaction Over Time (demo)", xaxis_title="Time (arbitrary units)", yaxis_title="Tx in mempool")
st.plotly_chart(fig, use_container_width=True)