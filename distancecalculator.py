import googlemaps
import csvhandler
import csv
import constants
gmaps = googlemaps.Client(key='insert your google maps api key here')

localizations = csvhandler.readLocalizations()

f = open(constants.DISTANCE_RESULT_PATH, 'w')
writer = csv.writer(f)
header = ["originCode",  "originLatitude" ,  "originLongitude", "destinyCode", "destinyLatitude" ,  "destinyLongitude", "distance"]
writer.writerow(header)

for originInstalationCode in localizations:
    originCoordinate = localizations[originInstalationCode]
    LatOrigin = originCoordinate[0]
    LongOrigin = originCoordinate[1]
    origins = (LatOrigin, LongOrigin)
    for destinyInstalationCode in localizations:
        destinyCoordinate = localizations[destinyInstalationCode] 
        LatDest = destinyCoordinate[0] 
        LongDest = destinyCoordinate[1]
        destination = (LatDest, LongDest)
        distance = gmaps.distance_matrix(origins, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
        writer.writerow([originInstalationCode,  LatOrigin , LongOrigin, destinyInstalationCode, LatDest, LongDest, distance])
