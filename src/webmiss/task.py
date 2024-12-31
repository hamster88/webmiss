from collections import Counter
from itertools import count
from random import uniform
import time

class Task:
    id:int = 0
    tid:int = 0
    title:str = ''
    summary:str = ''
    
    _counters = Counter()

    def __init__(self):
        cls = self.__class__
        self.id = Task._counters[cls]
        self.tid = Task._counters['tid']
        Task._counters[cls] += 1
        Task._counters['tid'] += 1
    
    def run(self):
        pass
    
    def start(self):
        try:
            self.run()
        except Exception as e:
            self.error = f'Abort in task: {self.summary}\n{e}'
    
    


class SleepTask(Task):
    delay = 1
    
    def __init__(self):
        super().__init__()
        self.delay = uniform(20, 50)
        self.title = f'Sleep_{self.delay:.0f}'
        self.summary = f'Sleep {self.delay} seconds'
        
    def run(self):
        print(f'start: {self.id} {self.title}')
        time.sleep(self.delay)
        print(f'done: {self.id} {self.title}')
        

class FetchTask(Task):
    url:str
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    from rich import inspect
    inspect(SleepTask())
    inspect(SleepTask())
    inspect(FetchTask())
    inspect(FetchTask())