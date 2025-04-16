from flask import Flask
from core.profit_engine import run_all_strategies
from monitor.strategy_dashboard import launch_dashboard
from core.roi_optimizer import optimize_loop

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ ARC_SUPERNOVA is alive and healthy", 200

# ✅ Run strategies automatically on app startup
launch_dashboard()
run_all_strategies()
optimize_loop()
