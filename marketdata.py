#!/usr/bin/env python3
# vim: set et ft=python fileencoding=utf_8 ts=4 sw=4:
# -*- coding: utf_8 -*-
"""Retrieves market data for crypto currencies.

Generates a `.csv` file,
outputting the result to the specified data directory, defaulting to
`$DATA_STORAGE_PATH/{CURRENT_DATE}T{CURRENT_TIME}_RH-CryptoHistoricalData.csv`.
"""

from datetime import datetime

from logger import setup_logger
from load_cfg import DATA_OUTPUT_DIRECTORY
# import robin_stocks.robinhood as rh


def generate_output_filename() -> str:
    """Return an output filename for Robinhood's cryptocoin historical data."""
    # Get current datetime.
    current_datetime: datetime = datetime.now()

    # Set current date.
    current_date: str = current_datetime.strftime("%Y-%m-%d")

    # Set current time.
    current_time: str = current_datetime.strftime("%H:%M:%S")

    # Construct the output filename.
    output_filename: str = \
        f"{current_date}T{current_time}_RH-CryptoHistoricalData.csv"

    # Return the output filename as a string.
    return output_filename


class MarketData:
    """A class representing the object generating market data."""

    def __init__(
        self,
        output_directory,
        output_filename=generate_output_filename()
    ):
        self.logger = setup_logger()
        self.output_directory = output_directory
        self.output_filename = output_filename

    @property
    def output_directory(self):
        self.logger.critical("Output directory: %s", self._output_directory)
        return self._output_directory

    @output_directory.setter
    def output_directory(self, value):
        self._output_directory = value

    @property
    def output_filename(self):
        self.logger.info("Output filename: %s", self._output_filename)
        return self._output_filename

    @output_filename.setter
    def output_filename(self, value=generate_output_filename()):
        self._output_filename = value


if __name__ == "__main__":
    market_data = MarketData(output_directory=DATA_OUTPUT_DIRECTORY)

    output_dir = market_data.output_directory
