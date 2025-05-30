class Appliance:
    def status(self):
        print("Appliance status unknown.")

class Fan(Appliance):
    def status(self):
        print("Fan is ON and running at medium speed.")

class Light(Appliance):
    def status(self):
        print("Light is ON with brightness level 70%.")

class AC(Appliance):
    def status(self):
        print("AC is cooling at 22°C.")

if __name__ == "__main__":
    devices = [Fan(), Light(), AC()]
    for device in devices:
        device.status()
