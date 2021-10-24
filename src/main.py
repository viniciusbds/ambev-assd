
import distributor
import productionsender
import reader

def ASSD(supplySites, depots):
    productionsender.sendProduction(supplySites)
    distributor.balanceDepots(depots)

def main():
    data = reader.readDataset()
    supplySites, depots = data[0], data[1]
    ASSD(supplySites, depots)

main()