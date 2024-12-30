from concurrent.futures import ThreadPoolExecutor
import threading


def run_worker(task, concurrent, delay=lambda:None):
    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        while True:
            if executor._work_queue.qsize() < 1:
                executor.submit(task)
            
            delay()
 

def start():
    thread_worker = threading.Thread(target=run_worker,daemon=True)
    thread_worker.start()
    
    return thread_worker