# Tracker Streamlit
 
# ASX Announcements Viewer

## Overview

This project is a Streamlit application designed to retrieve and display the 20 most recent announcements for a given list of ASX ticker symbols. The application allows users to filter and view announcements by selecting a specific ticker symbol and identifies tickers that have a "Trading Halt" announcement in their recent updates.

## Features

- **Retrieve Announcements:** Fetch the 20 most recent announcements for a predefined list of ASX ticker symbols using the provided API.
- **Filter by Ticker:** Users can select a ticker symbol from a sidebar dropdown to view announcements specific to that ticker.
- **Trading Halt Detection:** The application identifies and highlights any ticker symbols that have a "Trading Halt" announcement in their recent updates.

## API Details

The application uses the following API to fetch announcements for each ticker symbol:

https://www.asx.com.au/asx/1/company/{TICKER}/announcements?count=20&market_sensitive=false
Where {TICKER} is replaced with the relevant ticker symbol from the list.

## Ticker Symbols

The application works with the following ASX ticker symbols:

- AEE
- REZ
- 1AE
- 1MC
- NRZ

## How to Use

1. **Launch the Application:** Upon starting the Streamlit app, the user is presented with a simple interface.
2. **Select a Ticker:** Use the sidebar dropdown menu to select a ticker symbol. The 20 most recent announcements for the selected ticker will be displayed.
3. **View Announcements:** Announcements are shown in a table format with details including the release date, header, and a link to the full announcement.
4. **Check for Trading Halts:** The application will automatically check for any "Trading Halt" announcements and display a warning if such an announcement is found.


## Installation and Setup

To run this application locally:

1. Clone the repository from GitHub.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
