class Bank:
    def __init__(self,amount):
        self.amount = amount
    def getbalance(self):
        print("Current balance is : ", self.amount)
    def getdeposit(self,amount):
            self.amount = self.amount + amount
    def getwithdraw(self,amount):
                if self.amount >= amount:
                    self.amount = self.amount - amount
myobject = Bank(1000)
myobject.getbalance()
myobject.getdeposit(500)
myobject.getbalance()
myobject.getwithdraw(200)
myobject.getbalance()