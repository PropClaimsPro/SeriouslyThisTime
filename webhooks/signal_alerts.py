
import requests
def send_signal_alert(number, message):
    try:
        r = requests.post("http://localhost:8080/v2/send", json={"message": message, "number": number, "recipients": [number]})
        if r.status_code == 200:
            print("✅ Signal sent.")
        else:
            print(f"⚠️ Failed: {r.text}")
    except Exception as e:
        print(f"❌ Error sending Signal: {e}")
