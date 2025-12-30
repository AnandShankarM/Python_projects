from parking_lot import ParkingLot
from payment_machine import PaymentMachine

parking_lot = ParkingLot(5)
payment_machine = PaymentMachine()
is_running = True

while is_running:
    to_do = input("What do you want to do: ").lower()
    if to_do == "park":
        if parking_lot.park_car():
            if not payment_machine.take_payment():
                parking_lot.remove_car()
    elif to_do == "remove":
        parking_lot.remove_car()
    elif to_do == "report":
        parking_lot.report()
        payment_machine.report()
    elif to_do == "off":
         is_running = False
    