#!/usr/bin/env python3
"""
Description:
    A CLI utility to convert an amount from one currency to another using the ExchangeRate-API.

Requirements:
    - Python 3.x
    - requests

Installation:
    pip install requests

Usage:
    python currency_converter.py

    You will be prompted to enter:
    - Source currency code (e.g., INR)
    - Amount to convert
    - Target currency code (e.g., USD)

Note:
    - Replace api_key with your valid key from https://www.exchangerate-api.com/
    - Free tier has request limits.

Example:
    Enter the source currency e.g INR: INR  
    Enter the amount : 100  
    Enter the target currency e.g. USD: USD  
    Converted amount is: 1.20 USD

Author: Sachin Kumar
GitHub: https://github.com/sachin-py
"""

import requests


def fetch_conversion_rate(api_key, source_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency.upper()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('conversion_rates', {})
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None


def convert_currency():
    api_key = 'your-api-here'  # Replace with your actual API key

    source_currency = input(
        "Enter the source currency e.g INR: ").strip().upper()
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    target_currency = input(
        "Enter the target currency e.g. USD: ").strip().upper()

    conversion_rates = fetch_conversion_rate(api_key, source_currency)
    if not conversion_rates:
        return

    if target_currency not in conversion_rates:
        print(
            f"Currency '{target_currency}' not found in the conversion rates.")
        return

    exchange_rate = conversion_rates[target_currency]
    converted_amount = amount * exchange_rate
    print(f"Converted amount is: {converted_amount:.2f} {target_currency}")


if __name__ == "__main__":
    convert_currency()
