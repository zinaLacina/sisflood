from sis_model import FloodModel
from datetime import datetime,timedelta
import requests, os, json

DARK_SKY_API_KEY = os.environ['DARK_SKY_KEY']
option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si"

class FloodController:

    def getWeatherReport(self, date_from, date_to, latitude, longitude, city):
        d_from_date = datetime.strptime(date_from , '%Y-%m-%d')
        d_to_date = datetime.strptime(date_to , '%Y-%m-%d')
        delta = d_to_date - d_from_date

        latitude = str(latitude)
        longitude = str(longitude)

        weather_reports = []
