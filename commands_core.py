import os

def handle_builtin(command_line):
    args = command_line.split()
    if not args:
        return False

    cmd = args[0]

    if cmd == "cd":
        if len(args) < 2:
            print("cd: missing argument")
        else:
            try:
                os.chdir(args[1])
            except Exception as e:
                print(f"cd: {e}")
        return True

    elif cmd == "pwd":
        print(os.getcwd())
        return True

    elif cmd == "echo":
        print(" ".join(args[1:]))
        return True

    elif cmd == "clear":
        os.system('clear')
        return True

    # ...previous built-ins...

    elif cmd == "ls":
        for item in os.listdir():
            print(item)
        return True

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

    elif cmd == "mkdir":
        if len(args) < 2:
            print("mkdir: missing directory name")
        else:
            try:
                os.mkdir(args[1])
            except Exception as e:
                print(f"mkdir: {e}")
        return True

    elif cmd == "rmdir":
        if len(args) < 2:
            print("rmdir: missing directory name")
        else:
            try:
                os.rmdir(args[1])
            except Exception as e:
                print(f"rmdir: {e}")
        return True

    elif cmd == "rm":
        if len(args) < 2:
            print("rm: missing filename")
        else:
            try:
                os.remove(args[1])
            except Exception as e:
                print(f"rm: {e}")
        return True

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

    elif cmd == "kill":
        if len(args) < 2:
            print("kill: missing pid")
        else:
            try:
                os.kill(int(args[1]), 9)
            except Exception as e:
                print(f"kill: {e}")
        return True
    
    return False
