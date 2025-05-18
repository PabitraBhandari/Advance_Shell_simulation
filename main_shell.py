def main():
    while True:
        try:
            command = input("unixsim$ ")
            # Placeholder: just echoes command for now
            if command.strip() == "exit":
                print("Exiting shell.")
                break
            else:
                print(f"Received: {command}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting shell.")
            break

if __name__ == "__main__":
    main()
