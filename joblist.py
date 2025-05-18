# For minimal deliverable, just define empty or basic functions/classes
jobs = []

def add_job(pid, command):
    jobs.append({'pid': pid, 'command': command, 'status': 'Running'})

def list_jobs():
    for idx, job in enumerate(jobs):
        print(f"[{idx}] {job['command']} (PID: {job['pid']}, Status: {job['status']})")
