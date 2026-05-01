# Specification: End-to-End Agent Skeleton

## 1. Overview
This track focuses on creating a "walking skeleton" of the application. The goal is to establish a minimal, yet fully functional, end-to-end pipeline. This involves setting up the basic project structure, ensuring all core components (config, API client, Telegram bot) are connected, and can pass a single piece of live data from the train API to a Telegram message.

## 2. Functional Requirements
- The application must have a clear, organized file structure.
- It must load configuration from an external YAML or JSON file (e.g., `config.yaml`).
- It must successfully connect to and fetch data from the live train API for a single, hardcoded service.
- It must successfully connect to the Telegram Bot API and send a formatted message containing a piece of live data.
- The `README.md` must be updated with clear instructions on how to configure and run this skeleton application.

## 3. Out of Scope
- Complex business logic (e.g., predictive delays, route-wide monitoring, delay repay).
- Persistent data storage (no database).
- Advanced scheduling (a simple one-shot execution is sufficient).
- A comprehensive test suite (only minimal tests to prove connectivity).
