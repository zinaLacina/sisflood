class FloodModel():

    def __init__(self, date, precipType, 
                precipIntensityMax, summary, windSpeed, 
                icon):
        self.date = date
        self.precipType = precipType
        self.precipIntensityMax = precipIntensityMax
        self.summary = summary   
        self.windSpeed = windSpeed
        self.icon = icon 