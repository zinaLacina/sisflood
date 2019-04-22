class FloodModel():

    def __init__(self, date, precipType, 
                precipIntensityMax, summary, windSpeed, 
                icon,impact,raining_chance):
        self.date = date
        self.precipType = precipType
        self.precipIntensityMax = precipIntensityMax
        self.summary = summary   
        self.windSpeed = windSpeed
        self.icon = icon 
        self.impact = impact
        self.raining_chance = raining_chance