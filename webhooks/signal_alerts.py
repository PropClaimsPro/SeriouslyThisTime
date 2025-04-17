
import requests

def send_signal_alert(number, message):
    try:
        api_url = "http://localhost:8080/v2/send"
        payload = {
            "message": message,
            "number": number,
            "recipients": [number]
        }
        r = requests.post(api_url, json=payload)
        print(f"📤 Signal alert sent: {message}") if r.status_code == 200 else print(f"⚠️ Signal alert failed: {r.text}")
    except Exception as e:
        print(f"❌ Signal error: {e}")
