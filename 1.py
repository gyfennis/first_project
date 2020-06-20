from threading import *
from time import *

class MyThread(Thread):
    def __init__(self,song):
        self.song=song
        super().__init__()

    def run(self):
        for i in range(3):
            print("palying  %s %s" %(self.song,ctime()))
            sleep(2)

t=MyThread("亮亮")
t.start()
t.join()