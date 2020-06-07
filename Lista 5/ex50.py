class Product(object):
    id:int
    cost:float
    qtd:int = 0

    #SETs
    def setId(id):
        self.id = id
    def setCost(cost):
        self.cost = cost
    def setQtd(qtd):
        self.qtd = qtd

    #GETs
    def getId():
        return self.id
    def getCost():
        return self.cost
    def getQtd():
        return self.qtd

    #Methods
    def getTotal():
        return self.cost * self.qtd
    
    def addQtd(add):
        self.qtd += add

    def __str__(self):
        return '#{}:    {}  {:.2f} {:.2f}\n'.format(self.id, self.qtd, self.cost, self.getTotal())

    #def str(self):
        #return '#{}:    {}  {:.2f} {:.2f}\n'.format(self.id, self.qtd, self.cost, self.getTotal())

class Recipt:
    items = []

    def finalValue(self):
        tot = 0.0

#Main
qtd = int(input())

for i in range(qtd):
