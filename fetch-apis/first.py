import okx.MarketData as MarketData

flag = "0"  # Production trading:0 , demo trading:1

marketDataAPI =  MarketData.MarketAPI(flag=flag)

# Retrieve order book of the instrument
result = marketDataAPI.get_orderbook(
    instId="BTC-USDT"
)
print(result)
