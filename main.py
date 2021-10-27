import distributor
import rebalancer
import csvhandler

def ASSD(supplySites, depots):
    # First: send all production from Supply sites to all related CDDs
    distributor.sendProduction(supplySites, depots)
    csvhandler.saveResult("distribution-result",supplySites, depots)

    # Second: rebalance all CDDs if necessary
    rebalancer.balanceDepots(depots)
    csvhandler.saveResult("rebalance-result",supplySites, depots)

def main():
    data = csvhandler.readDataset()
    supplySites, depots = data[0], data[1]
    ASSD(supplySites, depots)

main()
