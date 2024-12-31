from webmiss import textual_main
from webmiss import worker
from webmiss import task

def main():
    worker.launch(task.SleepTask, 16)
    textual_main.MainApp().run()
    