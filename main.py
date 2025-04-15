from modules.vault_manager import VaultManager
from modules.ai_orchestrator import AIOrchestrator
from modules.quantum_optimizer import QuantumOptimizer
from modules.crypto_bot_launcher import CryptoBotLauncher
from modules.strategy_engine import StrategyEngine
from modules.db_logger import ProfitLogger

def main():
    print("🚀 Booting Profit Engine Phase II with AI, Quantum, Bots, and Vault-Connected SQLite DB")
    VaultManager().initialize(use_eth_wallet_assets=True)
    AIOrchestrator().launch_all_models()
    QuantumOptimizer().run()
    CryptoBotLauncher().deploy_all_trading_bots()
    StrategyEngine().start_all()
    ProfitLogger().initialize_db()
    ProfitLogger().log_event("Phase II App Booted")

if __name__ == "__main__":
    main()