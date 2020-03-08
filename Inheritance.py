class CreditCard:
    def __init__(self,customer,bank,account,limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def getCustomer(self):
        return self._customer
    def getBank(self):
        return self._bank
    def getAccount(self):
        return self._account
    def getLimit(self):
        return self._limit
    def getBalance(self):
        return self._balance

    def charge(self,price):
        """person takeing money from bank, increasing his balance in account"""
        if price+self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    def make_payment(self,amount):
        """person giving money to bank, decreasing his balance"""
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """Subclass in Inheritance"""
    def __init__(self,customer,bank,acnt,limit,apr):
        super().__init__(customer,bank,acnt,limit)  #super constructor call
        self._apr = apr

    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def greet(self):
        print("howdy!!!")



if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("Nitish","SBI","1234 1234 1234 1234",5000))
    wallet.append(CreditCard("Karan","IDBI","2345 2345 2345 2345",7000))
    wallet.append(CreditCard("Suman","ICICI","4545 4545 4545 4545",3500))

    for val in range(1,15):
        wallet[0].charge(val)
        wallet[1].charge(val*2)
        wallet[2].charge(val*3)

    for i in range(3):
        print("Customer\t",wallet[i].getCustomer())
        print("Bank\t",wallet[i].getBank())
        print("Account\t",wallet[i].getAccount())
        print("Limit\t",wallet[i].getLimit())
        print("Balance\t",wallet[i].getBalance())
        while(wallet[i].getBalance() > 100):
            wallet[i].make_payment(100)
            print("New Balance after payment of 200 \t",wallet[i].getBalance())
        print()

    pred = PredatoryCreditCard("Nitish","SBI","1234 1234 1234 1234",5000,12)
    print(pred.getBalance())
    print(pred.charge(6000))
    print(pred.getBalance())
    print(pred.charge(6000))
    print(pred.getBalance())


