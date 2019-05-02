import copy
import functools
import math


def createStatementData(invoice, plays):
    def playFor(aPerformance):
        return plays[aPerformance['playID']]
    
    def amountFor(aPerformance):
        """Calculate amount for the given performance"""
        result = 0
        if aPerformance['play']['type'] == "tragedy":
            result = 40000
            if aPerformance['audience'] > 30:
                result += 1000 * (aPerformance['audience'] - 30)
        
        elif aPerformance['play']['type'] == "comedy":
            result = 30000
            if aPerformance['audience'] > 20:
                result += 10000 + 500 * (aPerformance['audience'] - 20)
            result += 300 * aPerformance['audience']
        
        else:
            raise RuntimeError(f"unknown type: {aPerformance['play']['type']}")
        return result

    def volumeCreditsFor(aPerformance):
        result = 0
        result += max(aPerformance['audience'] - 30, 0)
        if "comedy" == aPerformance['play']['type']:
            result += math.floor(aPerformance['audience'] / 5)
        return result

    def enrichPerformance(aPerformance):
        calculator = PerformanceCalculator(aPerformance, playFor(aPerformance))
        result = copy.deepcopy(aPerformance)
        result['play'] = calculator.play
        result['amount'] = amountFor(result)
        result['volumeCredits'] = volumeCreditsFor(result)
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
