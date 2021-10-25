
distribution = {}   # key   = supplysiteCode + ":" + SKU + ":" + depotCode  
                    # value = amount of SKU (in Hl) to send from supplysiteCode to depotCode

def sendProduction(supplySites, depots):
    for key in supplySites:
        supplySite = supplySites[key]

        for SKU in supplySite.availableToDeploy:
            recipients = supplySite.recipients[SKU] # CDDs que estão na lista de envios da fábrica atual
            availableToDeploy = supplySite.availableToDeploy[SKU] 
            depotsSortedByNeed = sortDepotsByNeed(recipients, depots, SKU)

            priorityBasedDistribution(supplySite.code, SKU, availableToDeploy, depotsSortedByNeed)

    return distribution


# Ordena os depósitos de acordo com suas necessidades para o SKU, da maior para o menor
def sortDepotsByNeed(recipients, depots, SKU):
    resultList = []

    for depotCode in recipients:
        resultList.append(depots[depotCode])

    resultList.sort(key=lambda depot: depot.calculeNeed(SKU), reverse=True)

    return resultList


def priorityBasedDistribution(supplysite, SKU, availableToDeploy, depotsSortedByNeed):
    while availableToDeploy > 0:
        for depot in depotsSortedByNeed:
            priority = depot.calculeNeed(SKU)
            hectolitersToSend = 10 * priority

            if availableToDeploy < hectolitersToSend:
                hectolitersToSend = availableToDeploy
            
            sendFromTo(supplysite, depot, SKU, hectolitersToSend)
            availableToDeploy -= hectolitersToSend
        
    
def sendFromTo(supplysiteCode, depot, SKU, toSend):
    key = supplysiteCode + ":" + SKU + ":" + depot.code
    if key in distribution:
        distribution[key] += toSend
    else:
        distribution[key] = toSend
