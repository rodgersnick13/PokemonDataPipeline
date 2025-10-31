from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import PipelineSetup as pData

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')

@app.route('/')
def index():
    data = pData.pokeData().df
    result = data.to_json(orient='values')
    return result

if __name__ == '__main__':
    app.run()
