import streamlit as st
import pandas as pd
from data_announcenments import df_announcements  # Import the DataFrame

# List of ticker symbols to monitor
TICKERS = df_announcements['issuer_code'].unique()

# Function to check if any announcement contains the phrase "Trading Halt"
def check_trading_halt(announcements):
    return any("trading halt" in announcement.lower() for announcement in announcements)

# Streamlit App Layout
st.title("ASX Announcements Viewer")  # App title

# Sidebar for ticker selection
selected_ticker = st.sidebar.selectbox("Select a ticker symbol", TICKERS)  # Dropdown menu for selecting a ticker

# Filter announcements for the selected ticker
df_filtered = df_announcements[df_announcements['issuer_code'] == selected_ticker]

if not df_filtered.empty:  # If filtered data is not empty
    st.subheader(f"Announcements for {selected_ticker}")
    st.dataframe(df_filtered[['id', 'header', 'url']])  # Display relevant columns in a table

    # Check for any "Trading Halt" announcements in the filtered data
    if check_trading_halt(df_filtered['header']):
        st.warning("Trading Halt announcement detected!")  # Display a warning if a Trading Halt is detected
else:
    st.write("No announcements available for the selected ticker.")  # Inform the user if there are no announcements

# Display tickers that have "Trading Halt" announcements across all data
st.subheader("Tickers with Trading Halt Announcements")
halted_tickers = df_announcements[df_announcements['header'].str.contains("Trading Halt", case=False)]['issuer_code'].unique()

if len(halted_tickers) > 0:
    st.write(", ".join(halted_tickers))  # List tickers with Trading Halt announcements
else:
    st.write("No Trading Halt announcements detected.")
