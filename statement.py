import json
import math
import copy
from babel.numbers import format_currency

def renderPlainText(data, plays):
    """Render a statement in plain text and return the value"""

    def usd(aNumber):
        return format_currency(aNumber/100, "USD", locale="en_US")

    def totalVolumeCredits():
        result = 0
        for perf in data['performances']:
            result += perf['volumeCredits']
        return result

    def totalAmount():
        result = 0
        for perf in data['performances']:
            result += perf['amount']
        return result

    result = f"Statement for {data['customer']}\n"

    for perf in data['performances']:
        # print line for this order
        result += f"  {perf['play']['name']}: {usd(perf['amount'])} ({perf['audience']} seats)\n"

    result += f"Amount owed is {usd(totalAmount())}\n"
    result += f"You earned {totalVolumeCredits()} credits\n"
    return result

def statement(invoice, plays):
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
        result = copy.deepcopy(aPerformance)
        result['play'] = playFor(result)
        result['amount'] = amountFor(result)
        result['volumeCredits'] = volumeCreditsFor(result)
        return result

    statementData = {}
    statementData['customer'] = invoice['customer']
    statementData['performances'] = list(map(enrichPerformance, invoice['performances']))
    return renderPlainText(statementData, plays)

with open("plays.json", "r") as plays_file:
    plays = json.load(plays_file)

with open("invoices.json", "r") as invoices_file:
    invoices = json.load(invoices_file)

print(statement(invoices[0], plays))