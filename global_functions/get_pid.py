import psutil

def get_pid():
    process_name = "exefile.exe"
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return proc.info['pid']
    return None
