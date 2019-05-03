from performance import Performance

class Invoice:
    def __init__(self, aCustomer, thePerformances):
        self.customer = aCustomer
        self.performances = thePerformances

    def __getitem__(self, key):
        if key == "customer":
            return self.customer
        if key == "performances":
            return self.performances

    @staticmethod
    def decode(dct):
        if ("customer" in dct) & ("performances" in dct):
            return Invoice(dct['customer'], dct['performances'])
        return Performance.decode(dct)