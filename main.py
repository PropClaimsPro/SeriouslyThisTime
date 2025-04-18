from flask import Flask
from core.profit_engine import run_all_strategies
from core.roi_optimizer import optimize_loop
from core.self_evolve import evolve_if_needed

app = Flask(__name__)

@app.route("/")
def health():
    return "✅ ARC_SUPERNOVA PHASE 5: FINAL DEPLOYMENT READY"

run_all_strategies()
optimize_loop()
evolve_if_needed()
