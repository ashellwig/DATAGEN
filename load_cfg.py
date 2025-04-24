"""Creates the variables for constants needed throughout the application."""
from pathlib import Path
import os

from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# Set up API keys and environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
# Get working directory from environment variable
WORKING_DIRECTORY = os.getenv("WORKING_DIRECTORY", "./data_storage/")
# Get Conda-related paths from environment variables
CONDA_PATH = os.getenv("CONDA_PATH", "/home/user/anaconda3")
CONDA_ENV = os.getenv("CONDA_ENV", "base")
# Get ChromeDriver
CHROMEDRIVER_PATH = os.getenv(
    "CHROMEDRIVER_PATH",
    "./chromedriver/chromedriver"
)

# Setup Robinhood Integration

# Set authorization constants.
ROBINHOOD_USERNAME: str = os.getenv("ROBINHOOD_USERNAME")
ROBINHOOD_PASSWORD: str = os.getenv("ROBINHOOD_PASSWORD")

# Set output directory path.
DATA_OUTPUT_DIRECTORY: Path = Path(os.getenv("DATA_STORAGE_PATH"))
