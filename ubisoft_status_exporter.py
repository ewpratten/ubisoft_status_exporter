import requests
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    return "Ubisoft Status Exporter. See /metrics for data." 

@app.route("/metrics")
def metrics():
    
    # Make a request to the Ubisoft API
    # This will return a JSON list of game statuses
    ubi_response = requests.get("https://game-status-api.ubisoft.com/v1/instances")
    ubi_response_json = ubi_response.json()
    
    # Translate to prometheus format
    output = ["# HELP ubisoft_service_status A boolean value indicating if the service is up or down"]
    output.append("# TYPE ubisoft_service_status gauge")
    
    for game in ubi_response_json:
        app_id = game["AppID "] # Yes, there is a space in the key
        name = game["Name"]
        platform = game["Platform"]
        is_up = 1 if game["Status"] == "Online" else 0
        output.append(f'ubisoft_service_status{{app_id="{app_id}", name="{name}", platform="{platform}"}} {is_up}')

    return Response("\n".join(output), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
