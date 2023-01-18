# 14.10
import time
class timer():
    def __init__(self):
        self.initial_time=None
    def start(self):
        self.initial_time=time.time()
    def elapsed_seconds(self):
        return time.time()-self.initial_time
    def formatted_time(self,secs):
        mins=int(secs//60)
        secs=int(secs%60)
        return "{}:{:02d}".format(mins,secs)
t=timer()
t.start()
a=int(input("time : "))
time.sleep(a)
print(t.elapsed_seconds())
print(t.formatted_time(t.elapsed_seconds()))