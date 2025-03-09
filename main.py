# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Set page config
st.set_page_config(page_title="Time Zone App", page_icon="🕒")

# Apply custom CSS for black background and white text
st.markdown(
    """
    <style>
        body {
            background-color: black !important;
            color: white !important;
        }
        .stApp {
            background-color: black;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: white !important;
        }
        .stButton button {
            background-color: #444;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stTextInput, .stSelectbox, .stMultiSelect {
            background-color: #222;
            color: white;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🌍 Time Zone App")

# Multi-select time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

st.subheader("🕰 Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**:  {current_time}")

# Time conversion section
st.subheader("🔄 Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Convert button
if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {to_tz}: {converted_time}")
