import copy
import functools
import math


def createStatementData(invoice, plays):
    def playFor(aPerformance):
        return plays[aPerformance['playID']]

    def enrichPerformance(aPerformance):
        calculator = PerformanceCalculator(aPerformance, playFor(aPerformance))
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
        result = 0
        if self.play['type'] == "tragedy":
            result = 40000
            if self.performance['audience'] > 30:
                result += 1000 * (self.performance['audience'] - 30)
        
        elif self.play['type'] == "comedy":
            result = 30000
            if self.performance['audience'] > 20:
                result += 10000 + 500 * (self.performance['audience'] - 20)
            result += 300 * self.performance['audience']
        
        else:
            raise RuntimeError(f"unknown type: {self.play['type']}")
        return result

    amount = property(get_amount)

    def get_volumeCredits(self):
        result = 0
        result += max(self.performance['audience'] - 30, 0)
        if "comedy" == self.play['type']:
            result += math.floor(self.performance['audience'] / 5)
        return result

    volumeCredits = property(get_volumeCredits)