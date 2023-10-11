# Bulb test

class Bulb_example():
    status = 0

    def on(self):
        self.status = 1

    def off(self):
        self.status = 0

    def getStatus(self):
        if (self.status == 0):
            return 'Bulb is not glowing'
        elif (self.status == 1):
            return "Bulb is glowing"
    