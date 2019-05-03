from performance import Performance

class Invoice:
    def __init__(self, aCustomer, thePerformances):
        self.customer = aCustomer
        self.performances = thePerformances

    @staticmethod
    def decode(dct):
        if ("customer" in dct) & ("performances" in dct):
            return Invoice(dct['customer'], dct['performances'])
        return Performance.decode(dct)