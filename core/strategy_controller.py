
class StrategyController:
    def __init__(self):
        self.strategies = {
            "hft_ai_blitz_runner": True,
            "cross_exchange_arb_bot": True,
            "flashloan_strike_executor": True,
            "sentiment_signal_trader": True,
            "pumpdump_nexus_agent": True,
            "contentfarm_core": True,
            "retailscanner_exploitbot": True,
            "asi_global_coordinator": True,
        }

    def disable(self, name): self.strategies[name] = False
    def enable(self, name): self.strategies[name] = True
    def set_priority(self, name, weight): print(f"Priority of {name} set to {weight}")
