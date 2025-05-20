# Rasa Meeting Scheduler and Password Reset Bot

This project demonstrates a simple conversational AI assistant built using Rasa Open Source. The bot is designed to handle two main tasks: scheduling meetings and initiating password reset requests, along with standard conversational intents like greetings and goodbyes.

## Features

*   **Meeting Scheduling:** Guides the user through providing details like date, time, attendees, and location using a Rasa Form. Can also handle details provided upfront.
*   **Password Reset:** Collects an employee ID to initiate a notional password reset process.
*   **Standard Intents:** Responds to greetings, goodbyes, and confirms it is a bot when challenged.
*   **Out-of-Scope Handling:** Provides a generic response for queries outside its defined capabilities.
*   **Custom Actions:** Uses custom actions for the actual scheduling and password reset logic (simulated for this example).
*   **Form Validation:** Includes basic validation for meeting scheduling slots.

## Prerequisites

*   Python 3.6 or higher
*   Rasa Open Source
*   `rasa_sdk` (for running custom actions)

## Setup

1.  **Save the files:** Ensure the provided code snippets are saved in the correct structure within a project directory.
    *   Create a root directory (e.g., `my_rasa_bot`).
    *   Inside `my_rasa_bot`, create a `data` directory and place `stories.md` and `nlu.md` inside it.
    *   Inside `my_rasa_bot`, create an `actions` directory and place `actions.py` and `__init__.py` inside it.
    *   You will also need standard Rasa configuration files: `domain.yml` and `config.yml` in the root directory (`my_rasa_bot`). (Note: These files were not provided in the prompt, but are essential for a Rasa project. You would typically generate them using `rasa init` or create them based on your intents, entities, slots, actions, and utterances).

2.  **Navigate to the project directory:** Open your terminal or command prompt and change your current directory to the project root (e.g., `cd my_rasa_bot`).

3.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python -m venv .venv
    # On Windows
    .venv\Scripts\activate
    # On macOS/Linux
    source .venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install rasa rasa-sdk
    ```
    *(If you had a `requirements.txt` file listing dependencies like `rasa` and `rasa-sdk`, you would use `pip install -r requirements.txt`)*

## Running the Bot

Rasa bots typically involve two main components running in parallel: the Rasa Core/NLU process and the Action Server process (for custom actions).

1.  **Train the Rasa model:**
    ```bash
    rasa train
    ```
    This will train both the NLU and Core models based on your `data` files, `domain.yml`, and `config.yml`.

2.  **Run the Action Server:** Open a **new** terminal or command prompt window, navigate to your project directory, activate your virtual environment, and run the action server:
    ```bash
    rasa run actions
    ```
    This server will execute the code in your `actions/actions.py` file when triggered by the Rasa Core.

3.  **Talk to the bot:** Open a **third** terminal or command prompt window, navigate to your project directory, activate your virtual environment, and run the Rasa shell:
    ```bash
    rasa shell
    ```
    This command starts an interactive session in your terminal where you can chat with your bot. Ensure the action server (step 2) is running *before* you start the Rasa shell.

## Usage Examples

You can interact with the bot using phrases like:

*   **Greeting:** `hello`
*   **Schedule Meeting (step-by-step):** `schedule a meeting`
    *   Bot will ask for details like date, time, attendees, etc.
    *   Respond with: `tomorrow`, `3pm`, `John and Jane`, `conference room 5`
*   **Schedule Meeting (upfront):** `schedule a meeting tomorrow at 2pm with Alice in the meeting room`
*   **Password Reset:** `reset my password`
    *   Bot will ask for employee ID.
    *   Respond with: `E12345`
*   **Password Reset (upfront):** `reset my password for employee ID E9876`
*   **Bot Challenge:** `are you a bot?`
*   **Goodbye:** `bye`
*   **Out of Scope:** `what is the weather?`

## Project Files

*   `data/nlu.md`: Contains examples of user intents and how entities are extracted (e.g., `schedule_meeting`, `reset_password`, `inform`).
*   `data/stories.md`: Provides example conversations demonstrating typical user flows, including form usage and handling information provided upfront.
*   `actions/actions.py`: Contains the custom Python code for the bot's actions, including the `ActionScheduleMeeting`, `ActionResetPassword`, and the `ValidateScheduleMeetingForm` for cleaning and validating slot values during the form.
*   `actions/__init__.py`: An empty file marking the `actions` directory as a Python package.
*   `domain.yml` (required): Defines the bot's universe: intents, entities, slots, actions, forms, and responses. *(Not provided in the prompt, but necessary)*
*   `config.yml` (required): Configures the NLU and Core pipelines. *(Not provided in the prompt, but necessary)*

## License

This project is licensed under the MIT License - see the LICENSE.md file for details. *(Note: You might need to create a LICENSE.md file)*

## Acknowledgments

*   Built with Rasa Open Source.
