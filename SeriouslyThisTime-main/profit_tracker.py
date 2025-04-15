
import datetime

class ProfitTracker:
    def __init__(self):
        self.total_profit = 0.0

    def record_transaction(self, amount, source="unknown"):
        self.total_profit += amount
        print(f"[{datetime.datetime.now()}] +${amount:.2f} from {source} | Total: ${self.total_profit:.2f}")
        return self.total_profit

    def get_total(self):
        return self.total_profit
