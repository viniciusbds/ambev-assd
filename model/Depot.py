class Depot:

    def __init__(self, code, type, latitude, longitude):
        self.code = code
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = {}       # ex {"SKU1": (min, reorder, max)}
        self.closingStock = {}   # ex  {"SKU1": 1000,43 hl}
        self.orders = {}         # ex  {"SKU1": 1000,43 hl}


    def setLatitude(self, latitude):
        self.latitude = latitude


    def setLongitude(self, longitude):
        self.longitude = longitude


    def setSKUCapacity(self, sku, min, reorder, max):
        self.capacity[sku] += (min,reorder,max)


    def setSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] += closingStock

    
    def addDistributorOrder(self, sku, order):
        self.orders[sku] += order

