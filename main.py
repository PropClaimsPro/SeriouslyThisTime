from phase_v_replication import launch_phase_v_replication
from wallet_encryption import get_encrypted_wallet_key
import time

def main():
    print("[BOOTSTRAP] Launching Global Profit Engine")
    wallet = get_encrypted_wallet_key()
    print(f"[WALLET] Unlocked: {wallet}")
    launch_phase_v_replication()
    print("[ENGINE] Profit modules live.")
    while True:
        print("[PROFIT] ROI agents executing…")
        time.sleep(10)

if __name__ == "__main__":
    main()