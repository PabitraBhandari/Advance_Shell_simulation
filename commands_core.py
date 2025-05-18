# commands_core.py
# Implements built-in shell commands like cd, ls, etc.

import os
from joblist import list_jobs, bring_fg, resume_bg

def handle_builtin(command_line):
    """
    Checks if the command is built-in and executes it.
    Returns True if handled, False otherwise.
    """
    args = command_line.strip().split()
    if not args:
        return False  # No command to handle

    cmd = args[0]

    # Change directory
    if cmd == "cd":
        if len(args) < 2:
            print("cd: missing argument")
        else:
            try:
                os.chdir(args[1])
            except Exception as e:
                print(f"cd: {e}")
        return True

    # Print working directory
    elif cmd == "pwd":
        print(os.getcwd())
        return True

    # Print text to terminal
    elif cmd == "echo":
        print(" ".join(args[1:]))
        return True

    # Clear the terminal screen
    elif cmd == "clear":
        os.system('clear')
        return True

    # List files in the current directory
    elif cmd == "ls":
        for item in os.listdir():
            print(item)
        return True

    # Display file contents
    elif cmd == "cat":
        if len(args) < 2:
            print("cat: missing filename")
        else:
            try:
                with open(args[1], 'r') as f:
                    print(f.read())
            except Exception as e:
                print(f"cat: {e}")
        return True

    # Make a new directory
    elif cmd == "mkdir":
        if len(args) < 2:
            print("mkdir: missing directory name")
        else:
            try:
                os.mkdir(args[1])
            except Exception as e:
                print(f"mkdir: {e}")
        return True

    # Remove an empty directory
    elif cmd == "rmdir":
        if len(args) < 2:
            print("rmdir: missing directory name")
        else:
            try:
                os.rmdir(args[1])
            except Exception as e:
                print(f"rmdir: {e}")
        return True

    # Remove a file
    elif cmd == "rm":
        if len(args) < 2:
            print("rm: missing filename")
        else:
            try:
                os.remove(args[1])
            except Exception as e:
                print(f"rm: {e}")
        return True

    # Create an empty file or update its timestamp
    elif cmd == "touch":
        if len(args) < 2:
            print("touch: missing filename")
        else:
            try:
                with open(args[1], 'a'):
                    os.utime(args[1], None)
            except Exception as e:
                print(f"touch: {e}")
        return True

    # List all background jobs
    elif cmd == "jobs":
        list_jobs()
        return True

    # Bring a background job to foreground
    elif cmd == "fg":
        if len(args) < 2:
            print("fg: missing job id")
        else:
            bring_fg(args[1])
        return True

    # Resume a stopped job in background
    elif cmd == "bg":
        if len(args) < 2:
            print("bg: missing job id")
        else:
            resume_bg(args[1])
        return True

    return False  # Not a built-in command
