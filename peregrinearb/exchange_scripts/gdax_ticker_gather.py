from .ticker_gatherer import TickerGatherer


class GdaxTickerGatherer(TickerGatherer):

    def __init__(self, markets=None):
        if markets is None:
            markets = ['BTC-USD', 'ETH-USD', 'LTC-USD', 'BCH-USD', 'BTC-EUR', 'ETH-EUR', 'ETH-BTC', 'LTC-EUR',
                       'LTC-BTC', 'BCH-EUR', 'BCH-BTC']

        TickerGatherer.__init__(self, 'https://api.gdax.com/products/{}/book', markets)

    def format_tickers(self):
        self.logger.debug('Formatting tickers')
        result = {}
        for market, ticker in self.tickers:
            result['market'.replace('-', '/')] = {'bid': ticker['bids'][0][0], 'bidVolume': ticker['bids'][0][1],
                                                  'ask': ticker['asks'][0][0], 'askVolume': ticker['asks'][0][1]}
        self.logger.debug('Formatted tickers')

        return result