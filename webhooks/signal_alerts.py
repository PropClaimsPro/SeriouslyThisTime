
# Signal webhook (requires signal-cli-rest-api or local Signal CLI install)
import requests

def send_signal_message(number, message):
    api_url = "http://localhost:8080/v2/send"  # Assumes signal-cli-rest-api is running locally
    payload = {
        "message": message,
        "number": number,
        "recipients": [number]
    }
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            print(f"✅ Signal message sent to {number}")
        else:
            print(f"⚠️ Failed to send Signal message: {response.text}")
    except Exception as e:
        print(f"❌ Signal error: {e}")
