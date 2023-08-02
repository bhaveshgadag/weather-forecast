import streamlit as st
import plotly.express as px
from weather_api import get_data

st.title("Weather forecast of any city")
place = st.text_input("Enter city", key="place")
days = st.slider("Forecast days", key="days", min_value=1, max_value=5)
option = st.selectbox("Display option", options=['Temperature', 'Sky'])

st.subheader(f"{option} for next {days} days in {place}")

if place:
    data = get_data(place, days)

    if data == '404':
        st.warning('Please enter a valid city name.')

    elif option == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in data]
        dates = [dict['dt_txt'] for dict in data]
        figure = px.line(x=dates, y=filtered_data, labels={'x':'Dates', 'y':'Temperatures'})

        st.plotly_chart(figure)

    elif option == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in data]

        image_files = {
            "Clear":"images/clear.png",
            "Clouds":"images/cloud.png",
            "Rain":"images/rain.png",
            "Snow":"images/snow.png"
            }
        
        sky_images = [image_files[condition] for condition in filtered_data]
        st.image(sky_images, width=100)