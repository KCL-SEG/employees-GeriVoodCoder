"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, hours = 0, commission=0, commission_rate = 0):
        self.name = name
        self.pay = pay
        self.hours = hours
        self.commission = commission
        self.commission_rate = commission_rate

    def get_pay(self):
        total = 0
        if self.hours:
            total += self.pay * self.hours
        else:
            total += self.pay
        if self.commission:
            if self.commission_rate:
                total += self.commission * self.commission_rate
            else:
                total += self.commission
        return total

    def __str__(self):
        string = f"{self.name} works on a "
        if self.hours:
            string += f"contract of {self.hours} hours at {self.pay}/hour"
        else:
            string += f"monthly salary of {self.pay}"
        if self.commission:
            if self.commission_rate:
                string += f" and receives a commission for {self.commission_rate} contract(s) at {self.commission}/contract"
            else:
                string += f" and receives a bonus commission of {self.commission}"
        string += f".  Their total pay is {self.get_pay()}."
        return string

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600 )

print(robbie.get_pay())
print(str(robbie))
print(ariel.get_pay())
print(str(ariel))