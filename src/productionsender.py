import sender

def sendProduction(supplySites):
    #TODO
    for key in supplySites:
        supplySite = supplySites[key]

        print(supplySite)

        for SKU in supplySite.availableToDeploy:
            availableToDeploy = supplySite.availableToDeploy[SKU]
            depotsSortedByNeed = sortDepotsByNeed("", SKU)
            # print(SKU + " - " + availableToDeploy)

            priorityBasedDistribution(SKU, availableToDeploy, depotsSortedByNeed)

        print("----------")

def sortDepotsByNeed(depots, sku):
    # TODO
    pass

def priorityBasedDistribution(SKU, availableToDeploy, depotsSortedByNeed):
    while availableToDeploy > 0:
        for depot in depotsSortedByNeed:
            priority = depot.calculeNeed(SKU)
            hectolitersToSend = 10 * priority

            if availableToDeploy < hectolitersToSend:
                hectolitersToSend = availableToDeploy
            
            sender.sendTo(depot, SKU, hectolitersToSend)
            availableToDeploy -= hectolitersToSend