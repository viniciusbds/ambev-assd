import constants

class Depot:

    def __init__(self, code, type, latitude, longitude):
        self.code = code
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.capacity = {}       # ex  {"SKU1": (min, reorder, max)}
        self.closingStock = {}   # ex  {"SKU1": 999,99 hl}
        self.orders = {}         # ex  {"SKU1": 222,22 hl}
        self.averageDemand = {}  # ex  {"SKU1": 555,55 hl}


    #  Calcula a prioridade de um determinado SKU nesse depósito. O calculo é feito usando a seguinte formula:
    #  necessidade = 1 - nivelEstoque. Onde o nívelEstoque  = estoqueAtual / estoqueDesejado
    #  Dessa forma, quanto maior o nível de estoque, menor sua prioridade, e quanto menor o nível, maior a prioridade.
    def calculePriority(self, SKU):
        stockLevel = self.getStockLevel(SKU)
        if stockLevel != -1: 
            priority = 1 - stockLevel
        else: # no info about stockLevel available
            priority = 0.1 # prioridade baixa
        return max(priority,0)

    
    # Retorna a capacidade desejada desse Depósito, que pod ser: MIN, REORDER e MAX
    def desiredCapacity(self, SKU):

        if self.averageDemand[SKU] == 0:
            return ("min", -1)  # se a demanda não tem informações (0), use a capacidade mínima

        daysThatStockCanSupply = self.closingStock[SKU] / self.averageDemand[SKU]

        if daysThatStockCanSupply > constants.DAYS_CAN_SUPPLY_TOP:
            # como pode passar aproximadamente 15 dias com o estoque atual, 
            # entao a capacidade desejada para futuras demandas é a mínima
            cap = "min"
            desiredCap = self.capacity[SKU][0] 
        elif daysThatStockCanSupply > constants.DAYS_CAN_SUPPLY_MED and daysThatStockCanSupply < constants.DAYS_CAN_SUPPLY_TOP:
            # como pode passar aproximadamente entre 7 e 15 dias com o estoque atual,
            # entao a capacidade desejada para futuras demandas é a média (reorder)
            cap = "reorder"
            desiredCap = self.capacity[SKU][1]
        else:
            # como pode passar aproximadamente entre 0 e 7 dias com o estoque atual,
            # entao a capacidade desejada para futuras demandas é máxima
            cap = "max"
            desiredCap = self.capacity[SKU][2]

        return (cap, desiredCap)


    def getStockLevel(self, SKU):
        desiredCap = self.desiredCapacity(SKU)[1]
        closingStock = self.closingStock[SKU]

        if desiredCap > 0:
            stockLevel = closingStock / desiredCap
        else:
            stockLevel = -1  # caso desiredCap = 0, ou seja, nao temos informações

        return stockLevel


    def calculeExcedent(self, SKU):
        desiredCap = self.desiredCapacity(SKU)[1]
        closingStock = self.closingStock[SKU]
        maxStock = constants.IDEAL_STOCK_LEVEL * desiredCap
        if closingStock > maxStock:
            excedent = closingStock - maxStock
        else:
            excedent = 0
        return excedent

    
    def calculeNeed(self, SKU):
        desiredCap = self.desiredCapacity(SKU)[1]
        closingStock = self.closingStock[SKU]
        minimalStock = constants.CRITICAL_STOCK_LEVEL * desiredCap
        if closingStock < minimalStock:
            need = minimalStock - closingStock
        else:
            need = 0
        return need

    
    def saffetyRequest(self, SKU):
        stockLevel = self.getStockLevel(SKU) 
        desiredCap = self.desiredCapacity(SKU)[1]       
        closingStock = self.closingStock[SKU]
        if stockLevel > constants.IDEAL_STOCK_LEVEL:
            result = closingStock - desiredCap
        elif stockLevel > constants.SAFETY_MIN_STOCK_LEVEL:
            result = (stockLevel - constants.SAFETY_MIN_STOCK_LEVEL) * closingStock
        else:
            result = 0
        return result

    
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
    
    
    def addSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] += closingStock


    def removeSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] -= closingStock

    
    def setDistributorOrder(self, sku, order):
        self.orders[sku] = order
    

    def setAverageDemand(self, sku, averageDemand):
        self.averageDemand[sku] = averageDemand
    

    def __str__(self):
        return "code: " + self.code   + " capacity: " + str(self.capacity) + " closingStock: " + str(self.closingStock )

