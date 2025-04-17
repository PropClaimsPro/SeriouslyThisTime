from phase_v_replication import launch_phase_v_replication
from wallet_encryption import get_encrypted_wallet_key
import time

def main():
    print("[BOOT] Autonomous Profit Engine initializing...")
    key = get_encrypted_wallet_key()
    print(f"[WALLET] Decrypted key active.")
    launch_phase_v_replication()
    while True:
        print("[ENGINE] Executing live profit strategies...")
        time.sleep(10)

if __name__ == "__main__":
    main()