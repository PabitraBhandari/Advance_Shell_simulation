# joblist.py
# Manages tracking and status of background jobs for the shell

import os
import signal

# List of jobs. Each job is a dict with id, pid, command, process, and status.
jobs = []

def add_job(proc):
    """
    Adds a new background job to the jobs list.
    """
    job_id = len(jobs) + 1
    jobs.append({
        "id": job_id,
        "pid": proc.pid,
        "command": " ".join(proc.args),
        "process": proc,
        "status": "Running"
    })

def list_jobs():
    """
    Prints all currently tracked background jobs.
    """
    for job in jobs:
        status = job['status']
        print(f"[{job['id']}] {job['command']} (PID: {job['pid']}, {status})")

def update_job_status():
    """
    Updates the status of each background job, marking as 'Done' if finished.
    """
    for job in jobs:
        if job['status'] == "Running":
            ret = job['process'].poll()
            if ret is not None:
                job['status'] = "Done"

def bring_fg(job_id):
    """
    Brings a background job to the foreground (waits for it to finish).
    """
    for job in jobs:
        if str(job['id']) == str(job_id):
            if job['status'] == "Running":
                print(f"Bringing job [{job_id}] to foreground")
                job['process'].wait()
                job['status'] = "Done"
                return
            else:
                print(f"Job [{job_id}] is not running")
                return
    print(f"fg: No such job {job_id}")

def resume_bg(job_id):
    """
    Sends SIGCONT to resume a stopped job in the background.
    """
    for job in jobs:
        if str(job['id']) == str(job_id):
            if job['status'] == "Stopped":
                try:
                    os.kill(job['pid'], signal.SIGCONT)
                    job['status'] = "Running"
                    print(f"Resumed job [{job_id}] in background")
                except Exception as e:
                    print(f"bg: Error resuming job: {e}")
                return
            else:
                print(f"Job [{job_id}] is not stopped")
                return
    print(f"bg: No such job {job_id}")
