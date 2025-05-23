"""
Description:
    A simple script to convert an amount from one currency to another using the ExchangeRate-API.

Requirements:
    - Python 3.x
    - requests library

Installation:
    pip install requests

Usage:
    1. Replace api_key with your valid API key from https://www.exchangerate-api.com/
    2. Run the script
    3. When prompted, enter:
        - The source currency code (e.g., INR)
        - The amount to convert (e.g., 100)
        - The target currency code (e.g., USD)

Notes:
    - Ensure you have an internet connection.
    - API rate limits and key expiration apply as per ExchangeRate-API terms.
    - For production use, consider handling additional edge cases and errors.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

import requests

api_key = 'your-api=key-here'

source_currency = input('Enter the source currency e.g INR: ')
amount = float(input('Enter the amount : '))
target_currency = input('Enter the target currency e.g. USD: ')

url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    conversion_rates = data['conversion_rates']
    if target_currency in conversion_rates:
        exchange_rate = conversion_rates[target_currency]
        converted_amount = amount * exchange_rate
        print(f'Converted amount is {converted_amount} {target_currency}')
    else:
        print('Currency not found')
