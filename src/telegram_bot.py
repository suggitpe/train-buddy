"""
Placeholder for the Telegram bot client.
"""

# A simple in-memory list to simulate sent messages for testing purposes
_sent_messages = []

def send_message(chat_id: str, text: str):
    """
    Simulates sending a message to a Telegram chat.
    In this placeholder, it records the message in an in-memory list.
    """
    _sent_messages.append({"chat_id": chat_id, "text": text})

def get_sent_messages():
    """
    Returns the list of messages that have been "sent" by the placeholder bot.
    """
    return _sent_messages

def clear_sent_messages():
    """
    Clears the list of messages that have been "sent".
    """
    _sent_messages.clear()
