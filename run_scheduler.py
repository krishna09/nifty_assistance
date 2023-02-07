from nifty100.maintenance import Nifty100
from nifty200.maintenance import Nifty200
from nifty50.maintenance import Nifty50,calculate_time
import threading

def getThread(name,obj):
    return threading.Thread(name=name,target=obj.runMaintenance,daemon=True)

# n50  = Nifty50()
# n100 = Nifty100()
# n200 = Nifty200()

@calculate_time
def thread_call():
    objs = [Nifty50(), Nifty100(), Nifty200()]
    t_names = ["n50_thread","n100_thread","n200_thread"]
    nifty_threads = []
    for idx,obj in enumerate(objs):
        t=getThread(t_names[idx], obj)
        nifty_threads.append(t)
        print(f"\t\t\t\t{t_names[idx]} started..!!")
        t.start()
    for t in nifty_threads:
        t.join()
        print(f"\t\t\t\t{t.name} Completed..!!")

@calculate_time
def normal_call():
    objs = [Nifty50(), Nifty100(), Nifty200()]
    for obj in objs:
        obj.runMaintenance()

if __name__ == '__main__':
    # thread_call() # it is not working as expected "error if (shared._DFS[tkr]"
    normal_call()