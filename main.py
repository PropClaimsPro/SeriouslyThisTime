
from core.profit_engine import run_all_strategies
from core.strategy_controller import StrategyController
from monitor.strategy_dashboard import launch_dashboard
from core.roi_optimizer import optimize_loop

if __name__ == "__main__":
    print("🚀 ARC_SUPERNOVA SUPERSTACK LAUNCHED")
    launch_dashboard()
    run_all_strategies()
    optimize_loop()
