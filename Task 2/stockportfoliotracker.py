"""
CodeAlpha - Python Programming Internship
Task 2: Stock Portfolio Tracker

- User inputs stock names and quantities
- Hardcoded dictionary of stock prices
- Displays total investment value
- Saves the result to a .txt and .csv file
"""

import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 415,
    "META": 480,
    "NFLX": 650,
}


def show_available_stocks():
    print("Available stocks and prices (USD):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio():
    portfolio = {}
    print("Enter stock symbol and quantity. Type 'done' as the symbol to finish.\n")

    while True:
        symbol = input("Stock symbol: ").strip().upper()
        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the available stock list. Try again.\n")
            continue

        qty_input = input(f"Quantity of {symbol}: ").strip()
        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("Quantity must be a positive whole number.\n")
                continue
        except ValueError:
            print("Please enter a valid whole number for quantity.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    breakdown = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))
    return breakdown, total


def save_results(breakdown, total):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    txt_filename = f"portfolio_summary_{timestamp}.txt"
    csv_filename = f"portfolio_summary_{timestamp}.csv"

    with open(txt_filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 40 + "\n")
        for symbol, quantity, price, value in breakdown:
            f.write(f"{symbol}: {quantity} shares x ${price} = ${value}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")

    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Value (USD)"])
        for symbol, quantity, price, value in breakdown:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])

    print(f"\nResults saved to '{txt_filename}' and '{csv_filename}'.")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)

    print("\n--- Portfolio Summary ---")
    for symbol, quantity, price, value in breakdown:
        print(f"{symbol}: {quantity} shares x ${price} = ${value}")
    print("-" * 30)
    print(f"Total Investment: ${total}")

    save_choice = input("\nSave results to file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_results(breakdown, total)


if __name__ == "__main__":
    main()