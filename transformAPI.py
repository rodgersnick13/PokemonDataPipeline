from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import requests
import transform as t

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')

@app.route('/')
def index():

    response = requests.get("http://127.0.0.1:5000")
    result = t.Transform(response.json())
    return result.df.to_json()

if __name__ == '__main__':
    app.run(port=5001)
