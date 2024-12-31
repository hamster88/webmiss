from concurrent.futures import ThreadPoolExecutor
import threading

def run_worker(TaskClass, concurrent, delay=lambda:None):
    with ThreadPoolExecutor(max_workers=concurrent) as executor:
        while True:
            if executor._work_queue.qsize() < 1:
                t = TaskClass()
                executor.submit(t.start)

            delay()
            

def launch(TaskClass, concurrent, delay=lambda:None):
    thread_worker = threading.Thread(target=run_worker,args=(TaskClass, concurrent, delay),daemon=True)
    thread_worker.start()
    
    return thread_worker