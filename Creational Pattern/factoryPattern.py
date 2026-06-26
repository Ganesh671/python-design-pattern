
class Funds:

    def __init__(self,funds):
        self.funds = funds
        pass

    def print(self):
        print(self.funds)
    

class FundsFactory:

    def createTechFundsFactory(self):
        funds = ["APPL", "GOG", "AMAZ"]
        return Funds(funds)
    
    def createRetailFundFactory(self):
        funds = ["ITC","RYMD"]
        return Funds(funds)


fundFactory = FundsFactory()
fundFactory.createRetailFundFactory().print()

print("------- tech stocks----------")
fundFactory.createTechFundsFactory().print()