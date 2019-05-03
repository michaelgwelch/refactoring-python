import copy
import functools
import math
from abc import ABC, abstractmethod
from invoice import Invoice


def createStatementData(invoice, plays):
    def playFor(aPerformance):
        return plays[aPerformance.playID]

    def enrichPerformance(aPerformance):
        calculator = PerformanceCalculator.create(aPerformance, playFor(aPerformance))
        result = copy.deepcopy(aPerformance)
        result.play = calculator.play
        result.amount = calculator.amount
        result.volumeCredits = calculator.volumeCredits
        return result

    def totalVolumeCredits(data):
        return functools.reduce(
            lambda total, p: total + p.volumeCredits, data['performances'], 0)

    def totalAmount(data):
        return functools.reduce(
            lambda total, p: total + p.amount, data['performances'], 0)

    result = {}
    result['customer'] = invoice.customer
    result['performances'] = list(map(enrichPerformance, invoice.performances))
    result['totalAmount'] = totalAmount(result)
    result['totalVolumeCredits'] = totalVolumeCredits(result)
    return result


class PerformanceCalculator(ABC):
    def __init__(self, aPerformance, aPlay):
        self.performance = aPerformance
        self.play = aPlay

    @property
    @abstractmethod
    def amount(self):
        pass

    @property
    def volumeCredits(self):
        return max(self.performance.audience - 30, 0)

    @staticmethod
    def create(aPerformance, aPlay):
        if aPlay.type == "tragedy":
            return TragedyCalculator(aPerformance, aPlay)
        elif aPlay.type == "comedy":
            return ComedyCalculator(aPerformance, aPlay)
        else:
            raise RuntimeError(f"unknown type: {aPlay.type}")

class TragedyCalculator(PerformanceCalculator):
    def __init__(self, aPerformance, aPlay):
        super().__init__(aPerformance, aPlay)

    @property
    def amount(self):
        result = 40000
        if self.performance.audience > 30:
            result += 1000 * (self.performance.audience - 30)
        return result

class ComedyCalculator(PerformanceCalculator):
    def __init__(self, aPerformance, aPlay):
        super().__init__(aPerformance, aPlay)

    @property
    def amount(self):
        result = 30000
        if self.performance.audience > 20:
            result += 10000 + 500 * (self.performance.audience - 20)
        result += 300 * self.performance.audience
        return result

    @property
    def volumeCredits(self):
        return super().volumeCredits + math.floor(self.performance.audience / 5)

