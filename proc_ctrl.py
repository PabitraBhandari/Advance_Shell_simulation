# proc_ctrl.py
# Handles running external (non-built-in) commands and job management

import subprocess
import shlex
from joblist import add_job, update_job_status

def execute_external_command(command_line):
    """
    Runs an external command, supporting background jobs with &.
    """
    # Check if this is a background job (ends with '&')
    is_background = command_line.endswith('&')
    if is_background:
        command_line = command_line[:-1].strip()

    args = shlex.split(command_line)
    if not args:
        return  # No command to run

    try:
        if is_background:
            # Start process and do not wait; add to background jobs
            proc = subprocess.Popen(args)
            add_job(proc)
            print(f"Started background process PID: {proc.pid}")
        else:
            # Foreground: wait for process to finish
            proc = subprocess.Popen(args)
            proc.wait()
    except FileNotFoundError:
        print(f"{args[0]}: command not found")
    except Exception as e:
        print(f"Error: {e}")

def update_jobs_status():
    """
    Updates status of all background jobs (marks done if finished).
    """
    update_job_status()
