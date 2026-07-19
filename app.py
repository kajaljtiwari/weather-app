import requests
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY=os.getenv("WEATHER_API_KEY")
st.set_page_config(page_title="Weather App",page_icon="🌈")
st.title("Whether App ⛅")
st.write("Enter a city name and click the button to get the weather data")
city = st.text_input("Enter city name:")
API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

if st.button("Fetch weather Data"):
   response = requests.get(API_URL)
   if(response.status_code==200):
      st.success("Data Fetched succesfully ")
      data=response.json()
 
      #fetch the whether data in variables
      temperature = data["main"]["temp"]
      humidity = data["main"]["humidity"]
      wind_speed = data["wind"]["speed"]
      weather = data["weather"][0]["main"]

      col1,col2=st.columns(2)
      col3,col4=st.columns(2)
      col1.metric("Temperature",f" 🌡️{temperature}°C")
      col2.metric("Humidity",f" 💦{humidity}%")
      col3.metric("Wind_Speed",f" 🍃 {wind_speed}m/s")
      col4.metric("Weather",f"☁️{weather}")

   else:
      st.error("Invalid city name")


