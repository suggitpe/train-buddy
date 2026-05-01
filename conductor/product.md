# Initial Concept

i travel into london on EMR from kettering to st pancras daily. I usually catch the 6:36 train into london and then catch either the 18.05, 18:35 or 19.05 train home. I would like to build an agentic system that runs on a raspberry pi that does a few things. 1. it should look at the real time trains data and tell me if trains are running well for my line, and specifically if my trains are running and 2. if i am on a train that is delayed to craete my delay repay for me. i want it to communicate with me usin telegraph messaging and listen to responses from me for example leaving the office now

# Product Guide: Your Personal Train Buddy

## 1. Vision

To create a configurable and self-hostable commuting assistant that simplifies the daily train journey. The system will empower individual users to monitor their specific train services in real-time, receive timely updates, and automate the tedious process of claiming compensation for delays.

## 2. Target Audience

This project is for any commuter who is comfortable with basic technical setup (like running a project on a Raspberry Pi). While it will be developed and tested for one user's specific EMR commute, the core design goal is to create a template that other people can easily clone, configure for their own train routes, and run on their own hardware.

## 3. Core Features

*   **Easy Configuration:** The system will be designed for straightforward setup. Key variables such as train numbers, station codes, home/work locations, and API keys will be managed in a simple configuration file, allowing a new user to adapt the project for their own commute without altering the source code.
*   **Continuous & Dynamic Train Monitoring:** The agent will provide two layers of monitoring:
    *   **Specific Train Alerts:** It will monitor the user's configured primary trains (e.g., the 06:36 morning train) and send direct alerts if they are delayed or cancelled.
    *   **General Route Monitoring:** Throughout the day, the system will continuously monitor the overall health of the user's entire route (e.g., St Pancras to Kettering). If it detects significant, widespread delays or disruptions at any time, it will send a general alert. This allows the user to make proactive decisions, such as leaving work early to avoid worsening travel conditions.
*   **Automated Delay Repay Drafts:** In the event of a significant delay, the system will automatically gather the necessary journey details and pre-fill a "Delay Repay" claim.
*   **Interactive User Commands:** The user can communicate with the agent via simple text commands (e.g., "leaving the office now") to provide real-time context.

## 4. Platform & Interaction

*   **Hardware:** The agent is designed to run on a modern, low-power computer like a Raspberry Pi (Model 4, 5, or Zero 2 W) with an internet connection.
*   **Communication:** All communication will be handled through the Telegram messaging platform.