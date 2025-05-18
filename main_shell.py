import sys
from commands_core import handle_builtin

def main():
    while True:
        try:
            user_input = input("unixsim$ ").strip()
            if not user_input:
                continue  # Empty input, show prompt again

            if user_input == "exit":
                print("Exiting shell.")
                break

            # Check and run built-in commands
            if handle_builtin(user_input):
                continue

            # TODO: Add process creation and job control here (next steps)
            print(f"Unknown command: {user_input}")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting shell.")
            break

if __name__ == "__main__":
    main()
