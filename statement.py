import json
import math
from babel.numbers import format_currency

def statement(invoice, plays):
    """Prints a statement"""

    def amountFor(aPerformance, play):
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

    totalAmount = 0
    volumeCredits = 0
    result = f"Statement for {invoice['customer']}\n"

    for perf in invoice['performances']:
        thisAmount = amountFor(perf, playFor(perf))

        # add volume credits
        volumeCredits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == playFor(perf)['type']:
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += f"  {playFor(perf)['name']}: {format_currency(thisAmount/100, 'USD', locale='en_US')} ({perf['audience']} seats)\n"
        totalAmount += thisAmount

    result += f"Amount owed is {format_currency(totalAmount/100, 'USD', locale='en_US')}\n"
    result += f"You earned {volumeCredits} credits\n"
    return result


with open("plays.json", "r") as plays_file:
    plays = json.load(plays_file)

with open("invoices.json", "r") as invoices_file:
    invoices = json.load(invoices_file)

print(statement(invoices[0], plays))