import sys,os
# print(os.getcwd())
# print("sys.path before adding")
# print(sys.path)
# sys.path.append(os.getcwd())
# print("sys.path after adding")
# print(sys.path)
from nifty50.reader import Nifty50
from nifty100.reader import Nifty100
from nifty200.reader import Nifty200

n50 = Nifty50()
n100 = Nifty100()
n200 = Nifty200()

print("Nifty50 tail\n",n50.sixMonthsData.tail())
print("Nifty100 tail\n",n100.sixMonthsData.tail())
print("Nifty200 tail\n",n200.sixMonthsData.tail())


