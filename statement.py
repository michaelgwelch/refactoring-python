import json
from createStatement import createStatementData
from babel.numbers import format_currency
from performance import Performance

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
    invoices = json.load(invoices_file, object_hook=Performance.decode)


def renderHtml(data):
    result = f"<h1>Statement for {data['customer']}</h1>\n"
    result += "<table>\n"
    result += "<tr><th>play</th><th>seats</th><th>cost</th></tr>"
    for perf in data['performances']:
        result += f"  <tr><td>{perf['play']['name']}</td><td>{perf['audience']}</td>"
        result += f"<td>{usd(perf['amount'])}</td></tr>\n"

    result += "</table>\n"
    result += f"<p>Amount owed is <em>{usd(data['totalAmount'])}</em></p>\n"
    result += f"<p>You earned <em>{data['totalVolumeCredits']}</em> credits</p>\n"
    return result

def htmlStatment(invoice, plays):
    return renderHtml(createStatementData(invoice, plays))

print(statement(invoices[0], plays))
