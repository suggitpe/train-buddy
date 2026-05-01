"""
Main entry point for the Train Buddy agent.
"""
import config
from src import train_api
from src import telegram_bot

def main():
    """
    Main function to run the agent.
    """
    print("Train Buddy agent starting...")
    configuration = config.load_config()

    if configuration:
        # Assuming we are monitoring the first train in the config for now
        first_train = configuration["user_settings"]["trains"][0]
        service_id = first_train["service_uid"]

        train_data = train_api.get_train_service(service_id)

        if train_data:
            message = (
                f"Train {train_data['service_id']} ({train_data['std']} from "
                f"{train_data['origin']} to {train_data['destination']}) is "
                f"{train_data['etd']}."
            )
            telegram_bot.send_message(configuration["user_settings"]["telegram_chat_id"], message)
            print(f"Sent message to Telegram: {message}")
        else:
            print("Could not retrieve train data.")
    else:
        print("Failed to load configuration.")
    print("Train Buddy agent finished.")

if __name__ == "__main__":
    main()
