"""
Retrieves market data for crypto currencies and generates a `.csv` file,
outputting the result to the specified data directory, defaulting to
`$DATA_STORAGE_PATH/{CURRENT_DATE}T{CURRENT_TIME}_RH-CryptoHistoricalData.csv`
"""

from datetime import datetime
# import os

# from dotenv import load_dotenv
# import robin_stocks.robinhood as rh


def generate_output_filename() -> str:
    """
    Return an output filename for RobinHood's cryptocoin historical
    data as a string.

    Returns:
        output_filename (str): Output filename as a string.
    """

    # Get current datetime to keep consistent between the separate variables.
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


if __name__ == "__main__":
    print(generate_output_filename())
