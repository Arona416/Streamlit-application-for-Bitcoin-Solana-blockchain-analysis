import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

def make_tps_chart(samples, title=""):
    """
    Crée un graphique linéaire du TPS de Solana en utilisant la liste d'échantillons `samples`.
    Chaque échantillon couvre une période (en général 60s) et contient le nombre de transactions.
    """
    if not samples:
        return go.Figure()
    # Trier les échantillons du plus ancien au plus récent
    samples_rev = list(reversed(samples))
    # Générer une liste de timestamps pour chaque échantillon (intervalle d'une minute)
    now = datetime.utcnow()
    times = [now - timedelta(minutes=(len(samples_rev) - 1 - i)) for i in range(len(samples_rev))]
    # Calculer la valeur TPS pour chaque échantillon (transactions / secondes sur la période)
    tps_values = []
    for s in samples_rev:
        if s.get('numTransactions') is not None and s.get('samplePeriodSecs') is not None:
            tps_values.append(s['numTransactions'] / s['samplePeriodSecs'])
    # Construire la figure Plotly avec la courbe TPS
    fig = go.Figure(data=[go.Scatter(x=times, y=tps_values, mode='lines', name='TPS')])
    fig.update_layout(title=title, xaxis_title=None, yaxis_title="TPS")
    return fig

def make_mempool_chart(data_points, title=""):
    """
    Crée un graphique linéaire pour le nombre de transactions dans la mempool Bitcoin.
    `data_points` est une liste de dicts avec 'x' (timestamp Unix) et 'y' (nombre de transactions).
    """
    if not data_points:
        return go.Figure()
    # Conversion des timestamps en datetime et extraction des valeurs
    times = [datetime.utcfromtimestamp(pt['x']) for pt in data_points]
    counts = [pt['y'] for pt in data_points]
    fig = go.Figure(data=[go.Scatter(x=times, y=counts, mode='lines', name='Mempool TX')])
    fig.update_layout(title=title, xaxis_title=None, yaxis_title=None)
    return fig

def make_price_comparison_chart(btc_history, sol_history, title=""):
    """
    Crée un graphique comparant les prix de Bitcoin et Solana sur une période donnée.
    `btc_history` et `sol_history` sont des listes de dicts avec 'date' (datetime) et 'price'.
    """
    if not btc_history or not sol_history:
        return go.Figure()
    # S'assurer que les deux séries couvrent la même longueur (même nombre de points)
    n = min(len(btc_history), len(sol_history))
    btc_history = btc_history[:n]
    sol_history = sol_history[:n]
    dates = [entry['date'] for entry in btc_history]
    btc_prices = [entry['price'] for entry in btc_history]
    sol_prices = [entry['price'] for entry in sol_history]
    # Créer une figure avec deux axes Y (secondaire pour Solana)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=dates, y=btc_prices, name='BTC Price (USD)', line=dict(color='orange')), secondary_y=False)
    fig.add_trace(go.Scatter(x=dates, y=sol_prices, name='SOL Price (USD)', line=dict(color='blue')), secondary_y=True)
    # Configuration des axes et du titre
    fig.update_layout(title=title, legend_title_text=None)
    fig.update_yaxes(title_text="BTC Price (USD)", tickprefix="$", secondary_y=False)
    fig.update_yaxes(title_text="SOL Price (USD)", tickprefix="$", secondary_y=True)
    fig.update_xaxes(title_text=None)
    return fig
