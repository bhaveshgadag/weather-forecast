import streamlit as st
import plotly.express as px
from weather_api import get_data

st.title("Weather forecast of any city")
place = st.text_input("Enter city", key="place")
days = st.slider("Forecast days", key="days", min_value=1, max_value=5)
option = st.selectbox("Display option", options=['Temperature', 'Sky'])

st.subheader(f"{option} for next {days} days in {place}")

if place != '':
    data, dates = get_data(place, days, option)
    figure = px.line(x=dates, y=data, labels={'x':'Dates', 'y':'Temperatures'})

    st.plotly_chart(figure)