class Bankacc:
    def __init__(self, name, interest_rate, balance):
        self.name = name
        self.interest_rate = interest_rate
        self.balance = balance

    def simple_interest(self, years):
        print((self.balance*years*self.interest_rate)/100)

school = Bankacc("Rashika", 2.7, 3000)

school.simple_interest(4)

    
