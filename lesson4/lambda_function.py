import json
from urllib.request import urlopen


def close(message):
    return {
        'sessionAttributes': {},
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': message
            }
        }
    }


def call_quote_api(ticker):
    response = urlopen('https://api.iextrading.com/1.0/stock/{}/delayed-quote'.format(ticker))
    response = json.load(response)
    return response['delayedPrice']


def get_quote(request):
    slots = request['currentIntent']['slots']
    ticker = slots['ticker']
    price = call_quote_api(ticker)

    message = 'The last price (delayed) of ticker {} was {}'.format(ticker, price)
    return close(message)


def lambda_handler(event, context):
    intent = event['currentIntent']['name']

    if intent == 'GetQuote':
        return get_quote(event)

    return "Sorry, I'm not sure what you have in mind.  Please try again."
