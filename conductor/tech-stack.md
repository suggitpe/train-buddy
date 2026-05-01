# Technology Stack

This document outlines the technology stack for the Personal Train Buddy project. The choices prioritize simplicity, reliability, and low resource consumption suitable for running on a Raspberry Pi.

## 1. Programming Language

*   **Python:** The project will be written in Python. Its extensive library ecosystem, ease of use for scripting and data handling, and excellent support on Raspberry Pi make it the ideal choice.

## 2. Core Libraries

*   **google-generativeai:** The official Python SDK for the Google AI API, used to power the agent's core reasoning and language understanding with Gemini models.
*   **Requests:** This library will be used for making all HTTP requests to the real-time train data APIs.
*   **python-telegram-bot:** This will be used to handle all interactions with the Telegram Bot API, including sending alerts and receiving user commands.
*   **APScheduler (Advanced Python Scheduler):** This library will be integrated into the application to manage the scheduling of recurring tasks, such as the periodic checks for train statuses.

## 3. Data Storage

*   **SQLite:** A local, file-based SQLite database will be used for all persistent data storage. This includes storing user configuration, journey history for delay repay claims, and any other necessary state. It provides the power of a relational database without the overhead of a separate server process.

## 4. Dependencies

All Python dependencies will be managed using a `requirements.txt` file.
