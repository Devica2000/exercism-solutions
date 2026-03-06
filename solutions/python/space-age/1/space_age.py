class SpaceAge:
    period_mapping = {"Mercury": 0.2408467,
                     "Venus": 0.61519726,
                     "Earth": 1.0,
                     "Mars": 1.8808158,
                     "Jupiter": 11.862615,
                     "Saturn": 29.447498,
                     "Uranus": 84.016846,
                     "Neptune": 164.79132}
    earth_seconds = 31557600
    
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        mercury_period = SpaceAge.period_mapping["Mercury"]
        return round((self.seconds/(mercury_period * SpaceAge.earth_seconds)), 2)

    def on_venus(self):
        venus_period = SpaceAge.period_mapping["Venus"]
        return round((self.seconds/(venus_period * SpaceAge.earth_seconds)), 2)

    def on_earth(self):
        earth_period = SpaceAge.period_mapping["Earth"]
        return round((self.seconds/(earth_period * SpaceAge.earth_seconds)), 2)

    def on_mars(self):
        mars_period = SpaceAge.period_mapping["Mars"]
        return round((self.seconds/(mars_period * SpaceAge.earth_seconds)), 2)

    def on_jupiter(self):
        jupiter_period = SpaceAge.period_mapping["Jupiter"]
        return round((self.seconds/(jupiter_period * SpaceAge.earth_seconds)), 2)

    def on_saturn(self):
        saturn_period = SpaceAge.period_mapping["Saturn"]
        return round((self.seconds/(saturn_period * SpaceAge.earth_seconds)), 2)

    def on_uranus(self):
        uranus_period = SpaceAge.period_mapping["Uranus"]
        return round((self.seconds/(uranus_period * SpaceAge.earth_seconds)), 2)

    def on_neptune(self):
        neptune_period = SpaceAge.period_mapping["Neptune"]
        return round((self.seconds/(neptune_period * SpaceAge.earth_seconds)), 2)
        
        
