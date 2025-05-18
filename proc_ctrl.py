import subprocess
import shlex
from joblist import add_job

def execute_external_command(command_line):
    is_background = command_line.endswith('&')
    if is_background:
        command_line = command_line[:-1].strip()

    args = shlex.split(command_line)

    if is_background:
        proc = subprocess.Popen(args)
        print(f"Started background process PID: {proc.pid}")
        add_job(proc.pid, " ".join(args))


    try:
        if is_background:
            proc = subprocess.Popen(args)
            print(f"Started background process PID: {proc.pid}")
            # TODO: Add to joblist
        else:
            proc = subprocess.Popen(args)
            proc.wait()
    except FileNotFoundError:
        print(f"{args[0]}: command not found")
    except Exception as e:
        print(f"Error: {e}")
