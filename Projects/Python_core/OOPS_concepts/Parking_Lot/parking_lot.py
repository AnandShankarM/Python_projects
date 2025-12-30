class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_cars = 0

    def park_car(self):
        if self.parked_cars < self.capacity:
            self.parked_cars += 1
            print("Car parked successfully.")
            return True
        else:
            print("Sorry, parking lot is full.")
            return False

    def remove_car(self):
        if self.parked_cars > 0:
            self.parked_cars -= 1
            print("Car removed.")
        else:
            print("No cars to remove.")

    def report(self):
        print(f"Parked cars: {self.parked_cars}/{self.capacity}")
