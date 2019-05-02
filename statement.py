import json
from createStatement import createStatementData
from babel.numbers import format_currency

def usd(aNumber):
    return format_currency(aNumber/100, "USD", locale="en_US")


def renderPlainText(data):
    """Render a statement in plain text and return the value"""


    result = f"Statement for {data['customer']}\n"

    for perf in data['performances']:
        # print line for this order
        result += f"  {perf['play']['name']}: {usd(perf['amount'])} ({perf['audience']} seats)\n"

    result += f"Amount owed is {usd(data['totalAmount'])}\n"
    result += f"You earned {data['totalVolumeCredits']} credits\n"
    return result

def statement(invoice, plays):
    return renderPlainText(createStatementData(invoice, plays))

with open("plays.json", "r") as plays_file:
    plays = json.load(plays_file)

with open("invoices.json", "r") as invoices_file:
    invoices = json.load(invoices_file)


print(statement(invoices[0], plays))
