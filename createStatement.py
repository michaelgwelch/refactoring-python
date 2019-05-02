import copy
import functools
import math


def createStatementData(invoice, plays):
    def playFor(aPerformance):
        return plays[aPerformance['playID']]

    def enrichPerformance(aPerformance):
        calculator = PerformanceCalculator.create(aPerformance, playFor(aPerformance))
        result = copy.deepcopy(aPerformance)
        result['play'] = calculator.play
        result['amount'] = calculator.amount
        result['volumeCredits'] = calculator.volumeCredits
        return result

    def totalVolumeCredits(data):
        return functools.reduce(
            lambda total, p: total + p['volumeCredits'], data['performances'], 0)

    def totalAmount(data):
        return functools.reduce(
            lambda total, p: total + p['amount'], data['performances'], 0)

    result = {}
    result['customer'] = invoice['customer']
    result['performances'] = list(map(enrichPerformance, invoice['performances']))
    result['totalAmount'] = totalAmount(result)
    result['totalVolumeCredits'] = totalVolumeCredits(result)
    return result


class PerformanceCalculator:
    def __init__(self, aPerformance, aPlay):
        self.performance = aPerformance
        self.play = aPlay

    def get_amount(self):
        """Calculate amount for the given performance"""

        if self.play['type'] == "tragedy":
            raise RuntimeError("Use TragedyCalculator")
        
        elif self.play['type'] == "comedy":
            raise RuntimeError("Use ComedyCalculator")
        
        else:
            raise RuntimeError(f"unknown type: {self.play['type']}")


    amount = property(get_amount)

    def get_volumeCredits(self):
        result = 0
        result += max(self.performance['audience'] - 30, 0)
        if "comedy" == self.play['type']:
            result += math.floor(self.performance['audience'] / 5)
        return result

    volumeCredits = property(get_volumeCredits)

    @staticmethod
    def create(aPerformance, aPlay):
        if aPlay['type'] == "tragedy":
            return TragedyCalculator(aPerformance, aPlay)
        elif aPlay['type'] == "comedy":
            return ComedyCalculator(aPerformance, aPlay)
        else:
            raise RuntimeError(f"unknown type: {aPlay['type']}")

class TragedyCalculator(PerformanceCalculator):
    def __init__(self, aPerformance, aPlay):
        super().__init__(aPerformance, aPlay)

    def get_amount(self):
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        return result

    amount = property(get_amount)     

class ComedyCalculator(PerformanceCalculator):
    def __init__(self, aPerformance, aPlay):
        super().__init__(aPerformance, aPlay)

    def get_amount(self):
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
        return result

    amount = property(get_amount)