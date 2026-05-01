"""
Tests for the placeholder Telegram bot client.
"""
import unittest
from unittest.mock import MagicMock

# This import will fail initially, which is expected for TDD
from src.telegram_bot import send_message, get_sent_messages, clear_sent_messages

class TestTelegramBotClient(unittest.TestCase):
    """
    Test suite for the placeholder Telegram bot client.
    """

    def setUp(self):
        """
        Set up for each test. Clears the sent messages list.
        """
        clear_sent_messages()

    def test_send_message_placeholder(self):
        """
        Tests that the placeholder function 'sends' a message by recording it.
        """
        chat_id = "test_chat_id"
        message_text = "Hello from placeholder bot!"
        
        send_message(chat_id, message_text)
        
        sent_messages = get_sent_messages()
        self.assertEqual(len(sent_messages), 1)
        self.assertEqual(sent_messages[0]["chat_id"], chat_id)
        self.assertEqual(sent_messages[0]["text"], message_text)

if __name__ == '__main__':
    unittest.main()
