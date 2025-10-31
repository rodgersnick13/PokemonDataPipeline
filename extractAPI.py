from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import pandas as pd

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')

@app.route('/')
def index():
    url = 'https://raw.githubusercontent.com/rodgersnick13/PokemonDataPipeline/refs/heads/main/pokemon.csv'
    df = pd.read_csv("pokemon.csv")
    #df = pd.read_csv(url)
    result = df.to_json()
    return result

if __name__ == '__main__':
    app.run()
