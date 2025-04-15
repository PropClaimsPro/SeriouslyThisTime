import os
from application.strategies.latest_strategies import run_latest_profit_strategies
from application.wallet.fallback_wallet import get_active_wallet
from application.analytics.real_time_analytics import RealTimeAnalytics
from application.contracts.contract_autogen import auto_generate_and_sync_wallet_contracts
from application.integrations.crypto_trading import ccxt_executor

def full_autonomous_deployment():
    print("[INIT] Ultimate Profit Engine Booting...")
    analytics = RealTimeAnalytics()
    auto_generate_and_sync_wallet_contracts()
    run_latest_profit_strategies()

    wallet_address = os.getenv("ETH_WALLET_ADDRESS")
    if wallet_address:
        print(f"[WALLET] Trading bots synced to: {wallet_address}")
        ccxt_executor.auto_trade(wallet_address)
    else:
        print("[WARNING] Wallet address not found in environment variables.")

    print("[STATUS] All ROI compounding, profit-maximization, and vault systems are ACTIVE.")

if __name__ == "__main__":
    full_autonomous_deployment()