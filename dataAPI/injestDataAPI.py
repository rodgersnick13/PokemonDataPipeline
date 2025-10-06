from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
# Static information as a metric
metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def main():
   return "Hello, World!"

@app.route('/skip')

@metrics.do_not_track()
def skip():
   return "This endpoint is not tracked."

@app.route('/<item_type>')

@metrics.counter('invocation_by_type', 'Number of invocations by type', labels={'item_type': lambda: request.view_args['item_type']})
def by_type(item_type):
   return f"Item type: {item_type}"

@app.route('/long-running')

@metrics.gauge('in_progress', 'Long running requests in progress')
def long_running():
   return "This is a long-running request."

@app.route('/status/<int:status>')

@metrics.summary('requests_by_status', 'Request latencies by status', labels={'status': lambda r: r.status_code})

@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path', labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
   return f'Status: {status}', status
if __name__ == '__main__':
   app.run()