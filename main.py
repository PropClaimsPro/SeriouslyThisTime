from flask import Flask, jsonify
from modules.vault_manager import VaultManager
from modules.ai_orchestrator import AIOrchestrator
from modules.quantum_optimizer import QuantumOptimizer
from modules.crypto_bot_launcher import CryptoBotLauncher
from modules.strategy_engine import StrategyEngine
from modules.db_logger import ProfitLogger

app = Flask(__name__)
logger = ProfitLogger()

@app.route("/dashboard")
def dashboard():
    logs = logger.get_logs()
    return jsonify(logs)

def launch_app():
    VaultManager().initialize(use_eth_wallet_assets=True)
    AIOrchestrator().launch_all_models()
    QuantumOptimizer().run()
    CryptoBotLauncher().deploy_all_trading_bots()
    StrategyEngine().start_all()
    logger.initialize_db()
    logger.log_event("Phase II App Booted with Dashboard & High-Speed Strategies")
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    launch_app()