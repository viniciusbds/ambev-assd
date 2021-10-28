from model.SupplySite import SupplySite
from model.Depot import Depot
import csv
import constants
import pandas as pd


def readLocalizations():
    localizations = {}
    with open(constants.LOCATIONS_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip header
        for row in reader:
            instalationCode, latitude, longitude = row[0], row[1], row[2]
            localizations[instalationCode] = (latitude, longitude)
    return localizations


def readDistances():
    distances = {}
    with open(constants.DISTANCE_RESULT_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip header
        for row in reader:
            originCode, destinyCode, distance = row[0], row[3], row[6]
            key = originCode + ":" + destinyCode
            distances[key] = distance
    return distances


def readDataset():
    supplySites = {}
    depots = {}
    localizations = readLocalizations()
    with open(constants.DATASET_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip header
        for row in reader:

            supplySiteCode = row[0]
            SKU = row[1]
            locationCode = row[2]
            averageDemand = row[3]
            locationType = row[4]
            minDOC = row[5]
            reorderPoint = row[6]
            maxDOC = row[7]
            closingStock = row[8]
            availableToDeploy = row[9]
            distributorOrders = row[10]

            # parse quantitative vars to float
            averageDemand = float(averageDemand.replace(',','.'))
            minDOC = float(minDOC.replace(',','.'))
            reorderPoint = float(reorderPoint.replace(',','.'))
            maxDOC = float(maxDOC.replace(',','.'))
            closingStock = float(closingStock.replace(',','.'))
            availableToDeploy = float(availableToDeploy.replace(',','.'))
            distributorOrders = float(distributorOrders.replace(',','.'))

            if supplySiteCode in supplySites:
                supplySite = supplySites[supplySiteCode]
            else:
                latitude = localizations[supplySiteCode][0]
                longitude = localizations[supplySiteCode][1]
                supplySite = SupplySite(supplySiteCode, latitude, longitude)

            if locationCode in depots:
                depot = depots[locationCode]
            else:
                latitude = localizations[locationCode][0]
                longitude = localizations[locationCode][1]
                depot = Depot(locationCode,locationType, latitude, longitude)


            supplySite.setSKUsToDeploy(SKU, availableToDeploy)
            supplySite.addRecipient(SKU, depot.code)

            depot.setSKUCapacity(SKU, minDOC, reorderPoint, maxDOC)
            depot.setSKUClosingStock(SKU, closingStock)
            depot.setDistributorOrder(SKU,distributorOrders)
            depot.setAverageDemand(SKU, averageDemand)

            # Update or add a supplySite/Depot on data structure
            supplySites[supplySiteCode] = supplySite
            depots[locationCode] = depot

    return (supplySites, depots)


def saveResult(name, supplySites, depots):
    csvFileName = constants.RESULTS_DIR + "/" +name + ".csv"
    f = open(csvFileName, 'w')
    writer = csv.writer(f)

    header = ["supplySiteCode",  "SKU" , "locationCode", "averageDemand", "locationType", "minDOC", "reorderPoint", "maxDOC", "old closingStock",  "new closingStock", "availableToDeploy", "distributorOrders"]
    writer.writerow(header)

    with open(constants.DATASET_PATH, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip header
        for row in reader:
            supplySiteCode = row[0]
            SKU = row[1]
            locationCode = row[2]
            averageDemand = row[3]
            locationType = row[4]
            minDOC = row[5]
            reorderPoint = row[6]
            maxDOC = row[7]
            closingStock = row[8]
            availableToDeploy = supplySites[supplySiteCode].availableToDeploy[SKU]
            distributorOrders = row[10]

            newClosingStock = depots[locationCode].closingStock[SKU]

            writer.writerow([supplySiteCode,  SKU , locationCode,
            averageDemand, locationType, minDOC, reorderPoint, maxDOC,
            closingStock, newClosingStock, availableToDeploy, distributorOrders])

    
    xlsxFileName = constants.RESULTS_DIR + "/" +name + ".xlsx"
    pd.read_csv(csvFileName).to_excel(xlsxFileName)
    