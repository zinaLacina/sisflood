# coding: utf-8
from flood_model import FloodModel
from datetime import datetime,timedelta
import requests, os, json

# DARK_SKY_API_KEY = os.environ['DARK_SKY_KEY']
DARK_SKY_API_KEY = os.getenv('DARK_SKY_KEY', 'ac49424582fd2f061dd0f3ac9fe66076')
option_list = "exclude=currently,minutely,hourly,alerts&amp;units=si"

class FloodController:

    def getWeatherReports(self, date_from, date_to, latitude, longitude):
        d_from_date = datetime.strptime(date_from , '%Y-%m-%d')
        d_to_date = datetime.strptime(date_to , '%Y-%m-%d')
        delta = d_to_date - d_from_date

        latitude = str(latitude)
        longitude = str(longitude)

        weather_reports = []
        for i in range(delta.days+1):
            new_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d')
            search_date = new_date+"T00:00:00"
            response = requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY+"/"+latitude+","+longitude+","+search_date+"?"+option_list)
            json_res = response.json()
            report_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d %A')
            # unit_type = '°F' if json_res['flags']['units'] == 'us' else '°C'
            # min_temperature = str(json_res['daily']['data'][0]['apparentTemperatureMin'])+unit_type
            # max_temperature = str(json_res['daily']['data'][0]['apparentTemperatureMax'])+unit_type
            report_summary = json_res['daily']['data'][0]['summary']
            icon = json_res['daily']['data'][0]['icon']
            precip_intensity_max = json_res['daily']['data'][0]['precipIntensityMax']
            impact = 0
            if(precip_intensity_max>1.2 and precip_intensity_max<2):
                impact = 1
            if(precip_intensity_max>2):
                impact = 2
            wind_speed = json_res['daily']['data'][0]['windSpeed']
            if(wind_speed>30):
                impact = 1
            precip_type = None
            precip_prob = None
            raining_chance = None
            if'precipProbability' in json_res['daily']['data'][0] and 'precipType' in json_res['daily']['data'][0]:
                precip_type = json_res['daily']['data'][0]['precipType']
                precip_prob = json_res['daily']['data'][0]['precipProbability']
            if (precip_type == 'rain' and precip_prob != None):
                precip_prob *= 100
                raining_chance = "%.2f%%" % (precip_prob)

            flood = FloodModel(report_date,precip_type,precip_intensity_max,report_summary,wind_speed, icon,impact, raining_chance)        

            weather_reports.append(flood)
            #object list to JSON list
            json_reports = json.dumps([weather_report.__dict__ for weather_report in weather_reports])

        return json_reports
