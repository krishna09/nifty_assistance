from nifty100.maintenance import Nifty100
from nifty200.maintenance import Nifty200
from nifty50.maintenance import Nifty50

n50 = Nifty50()
n100 = Nifty100()
n200 = Nifty200()

n50.runMaintenance()
n100.runMaintenance()
n200.runMaintenance()