#!/bin/env python3

import configparser, argparse, os

from iexfinance.stocks import Stock

__author__ = "Bernd Wernerus"
__version__ = "0.1"

def cls():
    """ System independet console clear """
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    parser = argparse.ArgumentParser(description='Monitor a list of Stonks')
    parser.add_argument('symbols', metavar='SYM', nargs='+',
                        help='List of Stock Symbols (max. 100)')
    parser.add_argument('--config', default="stockmonitor.conf",
                        help='Path to config file (default: stockmonitor.conf')
    parser.add_argument('-d', default=True, action='store_true',
                        help='Development Mode: Use Sandbox dataprovider')

    args = parser.parse_args()

    config_main = configparser.ConfigParser()
    config_main.read(args.config)

    for f in config_main['stockmonitor']['include'].split(' '):
        config_main.read(f)

    if args.d:
        print(config_main.sections())
        print(args)
        token = config_main['iex-sandbox']['apitoken']
        iexversion = config_main['iex-sandbox']['iex_api']
    else:
        token = config_main['iex']['apitoken']

    stock_datasource = Stock(args.symbols, token=token, output_format='pandas')
    if args.d:
        stock_datasource.version = iexversion

    cls()
    print("StockMonitor " + __version__ + " by " + __author__ + "\n")
    new_dataframe = stock_datasource.get_quote()

    ticker = new_dataframe[['companyName', 'latestPrice', 'volume', 'open',
                            'close', 'isUSMarketOpen']]

    print(ticker)

if __name__ == "__main__":
    main()

