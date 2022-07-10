import numpy as np
import requests
import matplotlib.pyplot as plt


# A function to get the data from Alpha Vantage API


# A function to extract the x and y values of the dataset
def extract_x_y(ticker):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=full&apikey=RY9JPRE2OAC80KJL"
    r = requests.get(url)
    data = r.json()

    # print(data['Time Series (Daily)'])

    stock_prices = {}

    for i in data['Time Series (Daily)'].keys():
        stock_prices[i] = data['Time Series (Daily)'][i]['4. close']

    print stock_prices

    stock_prices = sorted(stock_prices.items())

    return stock_prices


# The root mean squared regression method
def calculate_rmse(y_true, y_pred):
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    return rmse


# Training method calls
stock_prices = extract_x_y('AAPL')

x, y = [], []

ctr = 0

for i in stock_prices:
    print(i[0] + " " + i[1])
    x.append(i[0])
    y.append(i[1])

plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AAPL')
plt.show()
