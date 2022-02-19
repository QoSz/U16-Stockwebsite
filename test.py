from iexfinance.stocks import Stock

a = Stock("TSLA", token="sk_7cb9aa988f2b4088a816a76f0383d6af")
d = a.get_quote()
price = d["latestPrice"]
print(price)
