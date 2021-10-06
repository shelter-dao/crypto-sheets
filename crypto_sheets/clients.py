import ccxt


class FTX_US(ccxt.ftx):
    def __init__(self):
        super().__init__()
        self.hostname = "ftx.us"
        # self.apiKey = os.environ.get("FTX_US_API_KEY")
        # self.secret = os.environ.get("FTX_US_SECRET_KEY")

    def fetch_price(self, ticker):
        return self.fetch_ticker(ticker)['info']['price']
