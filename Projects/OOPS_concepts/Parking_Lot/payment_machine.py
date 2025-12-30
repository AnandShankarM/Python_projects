class PaymentMachine:
    def __init__(self):
        self.total_collected = 0

    def take_payment(self):
        amount = int(input("Enter parking fee (₹): "))
        if amount >= 50:
            self.total_collected += amount
            print("Payment successful.")
            return True
        else:
            print("Insufficient payment.")
            return False

    def report(self):
        print(f"Total money collected: ₹{self.total_collected}")
