import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


images = {"Clear" : "images/clear.png", "Clouds" : "images/cloud.png",
            "Rain" : "images/rain.png", "Snow" : "images/snow.png"
            }

if place:
        #Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures , labels={"x" : "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)
        
        
    if option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
        filtered_paths = [images[condition] for condition in filtered_data]
        st.image(filtered_paths, width=115)