import json
import math
from babel.numbers import format_currency

def renderPlainText(data, invoice, plays):
    """Render a statement in plain text and return the value"""

    def amountFor(aPerformance):
        """Calculate amount for the given performance"""
        result = 0
        if playFor(aPerformance)['type'] == "tragedy":
            result = 40000
            if aPerformance['audience'] > 30:
                result += 1000 * (aPerformance['audience'] - 30)
        
        elif playFor(aPerformance)['type'] == "comedy":
            result = 30000
            if aPerformance['audience'] > 20:
                result += 10000 + 500 * (aPerformance['audience'] - 20)
            result += 300 * aPerformance['audience']
        
        else:
            raise RuntimeError(f"unknown type: {playFor(aPerformance)['type']}")
        return result

    def playFor(aPerformance):
        return plays[aPerformance['playID']]

    def volumeCreditsFor(aPerformance):
        result = 0
        result += max(aPerformance['audience'] - 30, 0)
        if "comedy" == playFor(aPerformance)['type']:
            result += math.floor(aPerformance['audience'] / 5)
        return result

    def usd(aNumber):
        return format_currency(aNumber/100, "USD", locale="en_US")

    def totalVolumeCredits():
        result = 0
        for perf in invoice['performances']:
            # add volume credits
            result += volumeCreditsFor(perf)
        return result

    def totalAmount():
        result = 0
        for perf in invoice['performances']:
            result += amountFor(perf)
        return result

    result = f"Statement for {invoice['customer']}\n"

    for perf in invoice['performances']:
        # print line for this order
        result += f"  {playFor(perf)['name']}: {usd(amountFor(perf))} ({perf['audience']} seats)\n"

    result += f"Amount owed is {usd(totalAmount())}\n"
    result += f"You earned {totalVolumeCredits()} credits\n"
    return result

def statement(invoice, plays):
    statement = {}
    return renderPlainText(statement, invoice, plays)

with open("plays.json", "r") as plays_file:
    plays = json.load(plays_file)

with open("invoices.json", "r") as invoices_file:
    invoices = json.load(invoices_file)


print(statement(invoices[0], plays))