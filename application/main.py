from application.profit_strategies import execute_all_strategies
from application.quantum_ai_models import quantum_optimize
from application.secure_vault import initialize_vault
from application.transaction_engine import automate_transactions
from application.wallet_integration import wallet_manager
from application.autonomous_youtube import integrate_youtube_strategies
from application.compliance_security import security_compliance_check

def main():
    initialize_vault()
    wallet_manager.setup_wallet()
    security_compliance_check.perform_all_checks()
    integrate_youtube_strategies.run_extraction_engine()
    execute_all_strategies()
    quantum_optimize.execute_autonomous_optimization()
    automate_transactions.begin_autonomous_transactions()

if __name__ == "__main__":
    main()