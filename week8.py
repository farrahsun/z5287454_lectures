import yfinance as yf
import pandas as pd

# Define the ticker symbol
tickerSymbol = '8630.T'

# Get the stock information
stock = yf.Ticker(tickerSymbol)

# Get the balance sheet
balance_sheet = stock.balance_sheet

# Convert the balance sheet to a Pandas DataFrame
df = pd.DataFrame(balance_sheet)

# Output the balance sheet to a CSV file
df.to_csv('sompo_holdings_balance_sheet.csv')

