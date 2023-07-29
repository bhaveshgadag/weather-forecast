import streamlit as st

st.title("Weather forecast of any city")
place = st.text_input("Enter city", key="place")
days = st.slider("Forecast days", key="days", min_value=1, max_value=5)
option = st.selectbox("Display option", options=['Temperature', 'Sky'])

st.subheader(f"{option} for next {days} days in {place}")