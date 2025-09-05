from flask import Flask, jsonify
from google.cloud import bigquery

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask + BigQuery on Cloud Run!"

@app.route("/data")
def get_data():
    client = bigquery.Client()

    query = """ query_job = client.query(query)  """
    results = query_job.result()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
