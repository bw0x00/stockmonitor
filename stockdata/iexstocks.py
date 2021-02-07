#!/bin/env python3
"""
Abstraction Layer for Stock Data sources
"""

from stocks import Stocks
from iexfinance.stocks import Stock


class IEXStocks(Stocks):
    _devel = None
    _region = None
    _stocklist=None

    def __init__(self, region="us", devel=False):
        super().__init__(region, devel)
        print(str(self._devel) + "-" + self._region)

    def get_current(self,symbols=None):
        if type(symbols) != list:
            raise TypeError
        for sym in symbols:
            pass



if __name__ == "__main__":
    a = IEXStocks()
    a.get_current(['a'])
    a.get_current('b')
