# Código responsável pela distribuição da produção das fábricas para os estoques:
# sejam estoques de fábricas ou centro de distribuições (CDDs)

def sendProduction(supplySites, depots):
    for key in supplySites:
        supplySite = supplySites[key]

        for SKU in supplySite.availableToDeploy:
            recipients = supplySite.recipients[SKU] # CDDs que estão na lista de envios da fábrica atual
            availableToDeploy = supplySite.availableToDeploy[SKU] 
            depotsSortedByNeed = sortDepotsByNeed(recipients, depots, SKU)
            priorityBasedDistribution(supplySite, SKU, availableToDeploy, depotsSortedByNeed)


# Ordena os depósitos de acordo com suas necessidades para o SKU, da maior para o menor
def sortDepotsByNeed(recipients, depots, SKU):
    resultList = []
    for depotCode in recipients:
        resultList.append(depots[depotCode])

    resultList.sort(key=lambda depot: depot.calculePriority(SKU), reverse=True)
    return resultList


def priorityBasedDistribution(supplysite, SKU, availableToDeploy, depotsSortedByNeed):
    while availableToDeploy > 0:
        for depot in depotsSortedByNeed:
            priority = depot.calculePriority(SKU)
            hectolitersToSend = 1 * priority
            if availableToDeploy < hectolitersToSend:
                hectolitersToSend = availableToDeploy
            
            sendFromTo(supplysite, depot, SKU, hectolitersToSend)
            availableToDeploy -= hectolitersToSend
        
    
def sendFromTo(supplysite, depot, SKU, toSend):
    supplysite.removeSKUsToDeploy(SKU, toSend)
    depot.addSKUClosingStock(SKU, toSend)
