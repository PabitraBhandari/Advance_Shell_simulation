# main_shell.py
# Entry point for the unixsim shell
# Handles the main loop, user input, and dispatching commands

from commands_core import handle_builtin
from proc_ctrl import execute_external_command, update_jobs_status

def main():
    """
    Main shell loop. Repeatedly prompts user for input and dispatches commands.
    """
    while True:
        try:
            user_input = input("unixsim$ ").strip()
            if not user_input:
                continue  # Ignore empty input
            if user_input == "exit":
                print("Exiting shell.")
                break

            # Try running as a built-in command
            if handle_builtin(user_input):
                continue

            # Try running as an external command (may be background job)
            execute_external_command(user_input)
            update_jobs_status()  # Clean up finished background jobs

        except (KeyboardInterrupt, EOFError):
            # Handle Ctrl+C or Ctrl+D gracefully
            print("\nExiting shell.")
            break

if __name__ == "__main__":
    main()
