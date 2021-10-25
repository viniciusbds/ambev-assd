
def balanceDepots(depots):
    for depot in depots:
        for SKU in depots.closingStock:
            status = checkSKULevel(depot, SKU)
            if status == "excess":
                distribute(depot, SKU)
            elif status == "critical":
                request(depot, SKU)
            else:
                pass


def distribute(depot, SKU):
    #TODO
    pass


def checkSKULevel(depot, SKU):
    pass


def request(depot, SKU):
    #TODO
    pass


def sortDepotsByTransportCost(originDepot, depots):
    # TODO
    pass


def calculateExcedent(depot, SKU):
    pass