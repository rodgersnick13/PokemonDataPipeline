from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import requests
import transform as t

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')

@app.route('/')
def index():

    response = requests.post("http://127.0.0.1:5000/")
    response = response.to_json(orient='values')
    result = t.Transform(response)
    return result

if __name__ == '__main__':
    app.run(port=5001)
