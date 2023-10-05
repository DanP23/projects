class Personalfi():
    def __init__(self, name: str, accounttype: str, balance: float, interestrate: float, lengthofexistance: 0, monthlycontribution: float):
        self.name = name
        self.accounttype = accounttype
        self.balance = balance
        self.interestrate = interestrate
        self.lengthofexistance = lengthofexistance
        self.monthlycontribution = monthlycontribution
    
    def make_deposit(self, deposit):
        self.balance = self.balance + deposit

    def make_withdrawl(self, withdrawl):
        self.balance = self.balance - withdrawl

    def growthprojection(self, duration):
        result = self.balance * (1 + self.interestrate / 12) ** (12 * duration)
        return '{:.2f}'.format(result)
        
    def change_reocurring_contribution(self):
        self.monthlycontribution = float(input("amount request: "))
        
