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

        if desiredCap > 0:
            stockLevel = closingStock / desiredCap
        else:
            # caso desiredCap = 0, ou seja, nao temos informações: adiciona 0.9
            # para a prioridade ser (1 - 0.9) == 0.1, uma prioridade baixa
            stockLevel = 0.9  

        priority = max(1 - stockLevel,0)
        # note que caso stockLevel > 1, prioridade = 0
        return priority

    
    # Retorna a capacidade desejada desse Depósito, que pod ser: MIN, REORDER e MAX
    def desiredCapacity(self, SKU):

        if self.averageDemand[SKU] == 0:
            return "min"  # se a demanda não tem informações (0), use a capacidade mínima

        daysThatStockCanSupply = self.closingStock[SKU] / self.averageDemand[SKU]

        if daysThatStockCanSupply > 15:
            # como pode passar aproximadamente 15 dias com o estoque atual, 
            # entao a capacidade desejada para futuras demandas é a mínima
            cap = "min" 
        elif daysThatStockCanSupply > 7 and daysThatStockCanSupply < 15:
            # como pode passar aproximadamente entre 7 e 15 dias com o estoque atual,
            # entao a capacidade desejada para futuras demandas é a média (reorder)
            cap = "reorder"
        else:
            # como pode passar aproximadamente entre 0 e 7 dias com o estoque atual,
            # entao a capacidade desejada para futuras demandas é máxima
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
    
    
    def addSKUClosingStock(self, sku, closingStock):
        self.closingStock[sku] += closingStock

    
    def setDistributorOrder(self, sku, order):
        self.orders[sku] = order
    

    def setAverageDemand(self, sku, averageDemand):
        self.averageDemand[sku] = averageDemand
    

    def __str__(self):
        return "code: " + self.code   + " capacity: " + str(self.capacity) + " closingStock: " + str(self.closingStock )

