import requests
import time
from config import DISCORD_WEBHOOK_URL

NOTIFICATION_DELAY = 3 
notification_queue = []

def send_discord_notification(message):
    """Queues and sends messages to Discord webhook."""
    notification_queue.append(message)
    process_queue()

def process_queue():
    """Processes notification queue with a delay to prevent spam."""
    while notification_queue:
        message = notification_queue.pop(0)
        try:
            requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
            print("✅ Notification sent to Discord!")
        except Exception as e:
            print(f"❌ Error sending Discord notification: {e}")
        time.sleep(NOTIFICATION_DELAY)
 
