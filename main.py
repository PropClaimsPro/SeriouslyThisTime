
from flask import Flask
from routes.status import status
from routes.debug import debug
from routes.trigger import trigger_phase
from routes.report import report
from webhooks.signal_alerts import send_signal_alert

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ ARC_SUPERNOVA is alive and healthy", 200

@app.route("/status")
def status_route():
    return status()

@app.route("/debug")
def debug_route():
    return debug()

@app.route("/trigger/<phase>")
def trigger_route(phase):
    return trigger_phase(phase)

@app.route("/report")
def report_route():
    return report()

@app.route("/signal")
def signal_ping():
    send_signal_alert("+15044203332", "[ARC_SUPERNOVA] Profit notification test")
    return "✅ Signal alert sent"
