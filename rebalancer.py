import constants
import csvhandler

distances = csvhandler.readDistances()

def balanceDepots(depots):
    for depotCode in depots:
        depot = depots[depotCode]
        for SKU in depot.closingStock:
            status = checkSKULevel(depot, SKU)
            if status == "excess":
                distribute(depot, SKU, depots)
            elif status == "critical":
                request(depot, SKU, depots)
            else:
                pass


def checkSKULevel(depot, SKU):
    stockLevel = depot.getStockLevel(SKU)
    if stockLevel > constants.IDEAL_STOCK_LEVEL:
        result = "excess"
    elif stockLevel < constants.CRITICAL_STOCK_LEVEL:
        result = "critical"
    else:
        result = "ok"
    return result


def distribute(depot, SKU, depots) :
    depotsSortedByTransportCost = sortDepotsByTransportCost(depot, depots)
    excedent = depot.calculeExcedent(SKU)
    index = 0
    while excedent > 0 and index < len(depotsSortedByTransportCost):
        currentDepot = depotsSortedByTransportCost[index]
        if SKU in currentDepot.closingStock:
            need = currentDepot.calculeNeed(SKU)
            if need < excedent:
                toSend = need
            else:
                toSend = excedent
            sendFromTo(depot, currentDepot, SKU, toSend)
            excedent -= toSend
        index += 1


def request(depot, SKU, depots):
    depotsSortedByTransportCost = sortDepotsByTransportCost(depot, depots)
    need = depot.calculeNeed(SKU)
    index = 0
    while need > 0 and index < len(depotsSortedByTransportCost):
        currentDepot = depotsSortedByTransportCost[index]
        if SKU in currentDepot.closingStock:
            currDepotCanSend = currentDepot.saffetyRequest(SKU)
            if currDepotCanSend > need:
                currDepotCanSend = need
            sendFromTo(currentDepot, depot, SKU, currDepotCanSend)
            need -= currDepotCanSend
        index += 1


def sortDepotsByTransportCost(originDepot, depots):
    resultList = []
    for key in depots:
        resultList.append(depots[key])
    resultList.sort(key=lambda destinyDepot: calculeTransportCost(originDepot, destinyDepot))
    return resultList


def calculeTransportCost(originDepot, destinyDepot):
        return distances[originDepot.code + ":" + destinyDepot.code]


def sendFromTo(originDepot, destinyDepot, SKU, toSend):
    originDepot.removeSKUClosingStock(SKU, toSend)
    destinyDepot.addSKUClosingStock(SKU, toSend)
