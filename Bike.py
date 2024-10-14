class Bike:
    def __init__(self):
        self.is_on = False

    def bike_is_on(self):
        return self.is_on

    def on_bike(self):
        self.is_on = True

    def off_bike(self):
        self.is_on = False
