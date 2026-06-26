

class Funds:
        def __init__(self):
            self.id = None
            self.name = None
            self.price = None
            
        def setId(self, id):
            self.id = id
        
        def setname(self,name):
            self.name = name
        
        def setprice(self,price):
            self.price = price

class FundsBuilder:
        def __init__(self):
            self.funds = Funds()

        def addId(self,id):
            self.funds.setId(id)
            return self
        
        def addname(self,name):
            self.funds.setname(name)
            return self
        
        def addPrice(self,price):
            self.funds.setprice(price)
            return self

        def build(self):
            return self.funds

""" fund = BuilderPattern.FundsBuilder() \
        .addId(1) \
        .addname("APPL") \
        .addPrice(2000) \
        .build()

fund2 = BuilderPattern.FundsBuilder() \
        .addId(1) \
        .addname("APPL2") \
        .addPrice(2000) \
        .build()

print(fund.id)
print(fund2.name) """
        


        