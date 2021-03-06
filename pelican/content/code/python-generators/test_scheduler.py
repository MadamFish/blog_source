import mthread
import scheduler
import time

class TestMicroThread(mthread.MicroThread):
    def __init__(self, number):
        self.num = number

    def step(self):
        print "Number:", self.num
        time.sleep(1)

mt1 = TestMicroThread(1)
mt2 = TestMicroThread(2)
mt3 = TestMicroThread(3)

ms = scheduler.Scheduler()
ms.add_microthread(mt1)
ms.add_microthread(mt2)
ms.add_microthread(mt3)

ms.run()

