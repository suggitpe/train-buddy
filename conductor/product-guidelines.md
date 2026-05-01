# Product Guidelines

This document outlines the style, tone, and conventions for the project to ensure consistency and clarity, especially for new contributors.

## 1. Documentation Style: Contributor-Focused

All documentation, particularly the main `README.md`, should be written with a new contributor in mind. The priority is to make it as easy as possible for someone to get the project set up and running on their own machine.

*   **Clarity over Brevity:** Explanations should be clear and explicit.
*   **Setup Guide:** The `README.md` must include a "Getting Started" or "Setup" section with step-by-step instructions.
*   **Configuration:** All configurable variables must be clearly documented.

## 2. Commit Message Style: Conventional Commits

Git commits shall follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. This creates an explicit and readable commit history.

Each commit message consists of a **header**, a **body**, and a **footer**.

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

*   **Types:** Must be one of the following: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`.
*   **Example:** `feat(monitoring): add real-time train status checking`

## 3. Communication Tone: Concise & Factual

The Telegram bot's communication with the user should be direct, efficient, and unambiguous.

*   **Focus on Data:** Messages should deliver key information without conversational filler.
*   **Clarity:** Avoid jargon or slang. Use universally understood terms.
*   **Examples:**
    *   `OK`: "Train 06:36 is delayed by 12 minutes. New estimated arrival: 07:48."
    *   `Not OK`: "Whoops! Looks like your train is running a little late today."
