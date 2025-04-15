from flask import Flask
from routes.profit import profit_routes
from modules.vault_manager import VaultManager
from modules.ai_orchestrator import AIOrchestrator
from modules.quantum_optimizer import QuantumOptimizer
from modules.crypto_bot_launcher import CryptoBotLauncher
from modules.strategy_engine import StrategyEngine
from modules.db_logger import ProfitLogger

app = Flask(__name__)
app.register_blueprint(profit_routes)

@app.route("/")
def home():
    return "✅ SkyVault Phase II Profit Engine LIVE"

if __name__ == "__main__":
    VaultManager().initialize(use_eth_wallet_assets=True)
    AIOrchestrator().launch_all_models()
    QuantumOptimizer().run()
    CryptoBotLauncher().deploy_all_trading_bots()
    StrategyEngine().start_all()
    ProfitLogger().initialize_db()
    ProfitLogger().log_event("SkyVault Phase II App Launched")
    app.run(host="0.0.0.0", port=8080)