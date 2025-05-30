class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def device_info(self):
        print(f"Device ID: {self.device_id}")

class Flyer:
    def fly(self):
        print("Flying the drone...")

class Drone(Device, Flyer):
    def __init__(self, device_id):
        Device.__init__(self, device_id)

    def capture_image(self):
        print("Capturing image...")

if __name__ == "__main__":
    drone1 = Drone("DRONE_001")
    drone1.device_info()
    drone1.fly()
    drone1.capture_image()
