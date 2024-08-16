import streamlit as st
import requests
import pandas as pd

# List of ticker symbols to monitor
TICKERS = ['AEE', 'REZ', '1AE', '1MC', 'NRZ']

# Function to fetch and parse announcements from the ASX for a given ticker
def fetch_announcements(ticker):
    url = f"https://www.asx.com.au/asx/1/company/{ticker}/announcements?count=20&market_sensitive=false"
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        try:
            return response.json()  # Parse and return JSON data if available
        except requests.exceptions.JSONDecodeError:
            st.error(f"Error parsing JSON for {ticker}")  # Display error if JSON parsing fails
            return None
    else:
        st.error(f"Failed to fetch data for {ticker}: {response.status_code}")  # Display error if request fails
        return None

# Function to check if any announcement contains the phrase "Trading Halt"
def check_trading_halt(announcements):
    return any("trading halt" in announcement['header'].lower() for announcement in announcements)

# Streamlit App Layout
st.title("ASX Announcements Viewer")  # App title

# Sidebar for ticker selection
selected_ticker = st.sidebar.selectbox("Select a ticker symbol", TICKERS)  # Dropdown menu for selecting a ticker

# Fetch announcements for the selected ticker
data = fetch_announcements(selected_ticker)

if data:  # If data was successfully fetched
    # Display the announcements for the selected ticker
    st.subheader(f"Announcements for {selected_ticker}")
    
    df = pd.DataFrame(data['data'])  # Convert announcements data to a DataFrame
    if not df.empty:  # Check if DataFrame is not empty
        st.dataframe(df[['document_release_date', 'header', 'url']])  # Display relevant columns in a table
    else:
        st.write("No announcements available.")  # Inform the user if there are no announcements

    # Check for any "Trading Halt" announcements in the data
    if check_trading_halt(data['data']):
        st.warning("Trading Halt announcement detected!")  # Display a warning if a Trading Halt is detected
else:
    st.write("No data available for the selected ticker.")  # Inform the user if data fetching failed

# Function to fetch and parse announcements for all tickers
def fetch_all_announcements():
    results = {}
    for ticker in TICKERS:
        data = fetch_announcements(ticker)
        if data:
            results[ticker] = data['data']  # Store the announcements data for each ticker
    return results

# Fetch announcements for all tickers
all_announcements = fetch_all_announcements()

# Display tickers that have "Trading Halt" announcements
st.subheader("Tickers with Trading Halt Announcements")
halted_tickers = [ticker for ticker, announcements in all_announcements.items() if check_trading_halt(announcements)]
if halted_tickers:
    st.write(", ".join(halted_tickers))  # List tickers with Trading Halt announcements
else:
    st.write("No Trading Halt announcements detected.")  # Inform the user if no Trading Halt announcements are found
