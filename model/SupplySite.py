class SupplySite:

    def __init__(self, code, latitude, longitude):
        self.code = code
        self.latitude = latitude
        self.longitude = longitude
        self.availableToDeploy = {}       # ex  {"SKU1": 10000,43 hl}   AVAILABLE TO DEPLOY
        self.capacity = {}                # ex  {"SKU1": (min, reorder, max)}
        self.closingStock = {}            # ex  {"SKU1": 1000,43 hl}
        self.recipients = {}              # ex  {"SKU1": set(destinatarios) 


    def setLatitude(self, latitude):
        self.latitude = latitude


    def setLongitude(self, longitude):
        self.longitude = longitude


    def setSKUsToDeploy(self, sku, number):
        self.availableToDeploy[sku] = number
    
    
    def removeSKUsToDeploy(self, sku, number):
        self.availableToDeploy[sku] -= number


    def setSKUCapacity(self, sku, min, reorder, max):
        self.capacity[sku] = (min,reorder,max)


    def setSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] = closingStock


    def addSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] += closingStock


    def addRecipient(self, sku, locationCode):
        if sku in self.recipients:
            self.recipients[sku].add(locationCode)
        else:
            self.recipients[sku] = set()
            self.recipients[sku].add(locationCode)

    
    def __str__(self):
        return "code: " + self.code  +  " recipients (" +  str(len(self.recipients)) +"): " + str(self.recipients) + " availableToDeploy: " + str(self.availableToDeploy) +  " closingStock: " + str(self.closingStock )
