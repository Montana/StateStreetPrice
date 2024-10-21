import yfinance as yf

data = yf.Ticker('STT').history(period="1mo")
print(data)
