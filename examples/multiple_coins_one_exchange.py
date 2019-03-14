import asyncio
from peregrinearb import load_exchange_graph, print_profit_opportunity_for_path, bellman_ford

loop = asyncio.get_event_loop()
for exchange in ['gemini', 'hitbtc', 'binance', 'bittrex', 'huobipro', 'poloniex', 'okex']:
# for exchange in ['hitbtc', 'okex']:
    print(exchange.upper())
    graph = loop.run_until_complete(load_exchange_graph(exchange, fees=True))
    paths = bellman_ford(graph, 'BTC', unique_paths=True)
    for path in paths:
        print_profit_opportunity_for_path(graph, path, starting_amount=100)
