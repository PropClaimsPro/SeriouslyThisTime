from flask import Flask
from routes.status import status
from routes.debug import debug
from routes.trigger import trigger_phase
from routes.report import report
from webhooks.signal_alerts import send_signal_alert
from core.profit_engine import run_all_strategies
from core.roi_optimizer import optimize_loop
from core.self_evolve import evolve_if_needed

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ ARC_SUPERNOVA Phase 4 is live"

@app.route("/status")
def route_status(): return status()

@app.route("/debug")
def route_debug(): return debug()

@app.route("/trigger/<phase>")
def route_trigger(phase): return trigger_phase(phase)

@app.route("/report")
def route_report(): return report()

@app.route("/signal")
def route_signal():
    send_signal_alert("+15044203332", "🧠 ARC_SUPERNOVA profit signal triggered.")
    return "✅ Signal sent"

run_all_strategies()
optimize_loop()
evolve_if_needed()
