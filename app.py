from flask import Flask, jsonify
from google.cloud import bigquery

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask + BigQuery on Cloud Run!"

@app.route("/data")
def get_data():
    client = bigquery.Client()

    query = """
        SELECT AgeGroup, TotalCustomers,TotalRevenue
        FROM `acoustic-apex-469415-m0.DAG.age_summary`
        LIMIT 10
    """
    query_job = client.query(query)  
    results = query_job.result()

    rows = [{"AgeGroup": row.AgeGroup, "TotalCustomers": row.TotalCustomers, "TotalRevenue": row.TotalRevenue} for row in results]
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
