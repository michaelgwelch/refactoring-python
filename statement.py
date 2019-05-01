import json
import math
from babel.numbers import format_currency

def statement(invoice, plays):
    """Prints a statement"""
    totalAmount = 0
    volumeCredits = 0
    result = f"Statement for {invoice['customer']}\n"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        thisAmount = 0

        if play['type'] == "tragedy":
            thisAmount = 40000
            if perf['audience'] > 30:
                thisAmount += 1000 * (perf['audience'] - 30)
        
        elif play['type'] == "comedy":
            thisAmount = 30000
            if perf['audience'] > 20:
                thisAmount += 10000 + 500 * (perf['audience'] - 20)
            thisAmount += 300 * perf['audience']
        
        else:
            raise RuntimeError(f"unknown type: {play['type']}")

        # add volume credits
        volumeCredits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play['type']:
            volumeCredits += math.floor(perf['audience'] / 5)

        # print line for this order
        result += f"  {play['name']}: {format_currency(thisAmount/100, 'USD', locale='en_US')} ({perf['audience']} seats)\n"
        totalAmount += thisAmount

    result += f"Amount owed is {format_currency(totalAmount/100, 'USD', locale='en_US')}\n"
    result += f"You earned {volumeCredits} credits\n"
    return result





with open("plays.json", "r") as plays_file:
    plays = json.load(plays_file)

with open("invoices.json", "r") as invoices_file:
    invoices = json.load(invoices_file)

print(statement(invoices[0], plays))