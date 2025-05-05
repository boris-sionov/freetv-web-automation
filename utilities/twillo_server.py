from twilio.rest import Client
from bidi.algorithm import get_display
import arabic_reshaper
import time

from config import ConfigReader

account_sid = ConfigReader.read_config("twillo", "sid")
auth_token = ConfigReader.read_config("twillo", "token")

client = Client(account_sid, auth_token)

seen_message_sids = set()
while True:
    messages = client.messages.list(limit=100)

    for msg in messages:
        if msg.sid not in seen_message_sids:
            print(f"\n📩 New message:")
            print(f"From: {msg.from_}")
            print(f"To: {msg.to}")
            print(f"Time (UTC): {msg.date_sent.strftime(ConfigReader.read_config('date', 'twillo_time_format'))}")
            original_text = msg.body
            reshaped_text = arabic_reshaper.reshape(original_text)
            bidi_text = get_display(arabic_reshaper.reshape(msg.body))
            print(f"Body: {get_display(arabic_reshaper.reshape(msg.body))}")
            seen_message_sids.add(msg.sid)
    time.sleep(5)  # check every 5 seconds
