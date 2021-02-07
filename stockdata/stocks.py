#!/bin/env python3
"""
Abstraction Layer for Stock Data sources
"""

class Stocks():
    _devel = None
    _region = None

    def __init__(self, region="us", devel=False):
        self._devel = devel
        self._region = region

    def get_current(self, symbols):
        """ Returns a dictionary of the current values for provided symbols """
        pass


if __name__ == "__main__":
    pass
