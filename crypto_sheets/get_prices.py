import logging
import os

from .clients import FTX_US

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)d %(levelname)s: %(message)s',
    datefmt='%H:%M:%S',
)


def main():
    ftx_us = FTX_US()
    price = ftx_us.fetch_price(ticker='BTC/USD')
    logging.info(f"BTC/USD: {price}")

if __name__ == '__main__':
    main()
