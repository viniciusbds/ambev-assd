class Depot:

    def __init__(self, code, type, latitude, longitude):
        self.code = code
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = {}       # ex {"SKU1": (min, reorder, max)}
        self.closingStock = {}   # ex  {"SKU1": 1000,43 hl}
        self.orders = {}         # ex  {"SKU1": 1000,43 hl}
        self.averageDemand = {}  # ex  {"SKU1": 1000,43 hl}


    #  Calcula a necessidade de um determinado SKU nesse depósito. O calculo é feito usando a seguinte formula:
    #  necessidade = 1 - nivelEstoque. Onde o nívelEstoque  = estoqueAtual / estoqueDesejado
    #  Dessa forma, quanto maior o nível de estoque, menor sua prioridade, e quanto menor o nível, maior a prioridade.
    def calculeNeed(self, SKU):
        desiredCapLabel = self.desiredCapacity(SKU)

        if desiredCapLabel == "min":
            desiredCap = self.capacity[SKU][0]
        elif desiredCapLabel == "reorder":
            desiredCap = self.capacity[SKU][1]
        else:
            desiredCap = self.capacity[SKU][2]

        closingStock = self.closingStock[SKU]

        stockLevel = (closingStock / desiredCap)

        return 1 - stockLevel


    
    def desiredCapacity(self, SKU):

        if self.averageDemand[SKU] == 0:
            return "min"

        daysThatStockCanSupply = self.closingStock[SKU] / self.averageDemand[SKU]

        if daysThatStockCanSupply > 15:
            cap = "min"
        elif daysThatStockCanSupply > 7 and daysThatStockCanSupply < 15:
            cap = "reorder"
        else:
            cap = "max"

        return cap

    

    def getCapacityLevel(self, SKU):
        stock = self.closingStock[SKU]


    def setLatitude(self, latitude):
        self.latitude = latitude


    def setLongitude(self, longitude):
        self.longitude = longitude


    def setSKUCapacity(self, sku, min, reorder, max):
        self.capacity[sku] = (min,reorder,max)


    def setSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] = closingStock

    
    def setDistributorOrder(self, sku, order):
        self.orders[sku] = order
    

    def setAverageDemand(self, sku, averageDemand):
        self.averageDemand[sku] = averageDemand
    

    def __str__(self):
        return "code: " + self.code   + " capacity: " + str(self.capacity) + " closingStock: " + str(self.closingStock )

