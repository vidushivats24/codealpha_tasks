stock_prices = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 420,
    "TSLA": 200,
    "AMZN": 175
}

portfolio_value = 0

print("===== Stock Portfolio Tracker =====")

num_stocks = int(input("How many stocks do you own? "))

for i in range(num_stocks):
    stock_name = input("Enter stock symbol (AAPL, GOOGL, MSFT, TSLA, AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        value = stock_prices[stock_name] * quantity
        portfolio_value += value
        print(f"{stock_name}: ₹{value}")
    else:
        print("Stock not found in database.")

print("\n===== Portfolio Summary =====")
print("Total Portfolio Value: ₹", portfolio_value)
