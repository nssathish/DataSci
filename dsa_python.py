import math
from functools import reduce


class ATM:
    def __init__(self, pin: str):
        self._balance = 0
        self._pin = 1234
        self._validate_user(pin)

    def _validate_user(self, pin: str) -> bool:
        try:
            return True if int(pin) == self._pin else False
        except ValueError:
            print("Invalid PIN")

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def withdraw(self, amount: int) -> float:
        try:
            if self._empty():
                raise ValueError("Insufficient balance")
            elif amount > self._balance:
                raise ValueError("Amount exceeds balance")
            else:
                self._balance -= amount
                return float(self._balance)
        except ValueError as ve:
            print(ve)

    def _empty(self) -> bool:
        return self._balance == 0

    def _check_balance(self) -> float:
        return self._balance


class Calculator:
    def __init__(self, number1=1, number2=1):
        self._number1 = number1
        self._number2 = number2

    # 1. Addition
    def add(self):
        return self._number1 + self._number2

    # 2. Subtraction
    def subtract(self):
        return abs(self._number1 - self._number2)

    # 3. Multiplication
    def multiply(self):
        return self._number1 * self._number2

    # 4. Division
    def divide(self):
        numerator = self._number1
        denominator = self._number2
        try:
            if denominator == 0:
                raise "Denominator cannot be 0"
            else:
                return numerator / denominator
        except ValueError as ve:
            print(ve)

    # 5. power
    def power(self, number, exponent):
        return number**exponent

    # 6. square root
    def square_root(self, number):
        return math.sqrt(number)

    # 7. factorial
    def factorial(self, number):
        try:
            if number < 0:
                raise "number should be positive"
            elif number in [0, 1]:
                return 1
            else:
                return reduce(lambda x, y: x * y, list(range(1, number + 1)))
        except ValueError as ve:
            print(ve)

    # 8. fibonacci
    def fibonacci(self, n):
        try:
            if n <= 0:
                raise "number should be positive and more than 0"
            elif n == 1:
                return 0
            elif n in (2, 3):
                return 1
            else:
                previous = 1
                current = 1
                for i in range(3, n):
                    previous, current = current, current + previous
                return current
        except ValueError as ve:
            print(ve)


calc = Calculator(2, 3)
print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())
print(calc.power(2, 3))
print(calc.fibonacci(1))
print(calc.fibonacci(2))
print(calc.fibonacci(3))
print(calc.fibonacci(5))
print(calc.fibonacci(11))

# if __name__ == "__main__":
#     hdfc_atm = ATM("1234")
#     hdfc_atm.deposit(100)
#     hdfc_atm.deposit(1000)
#     print(hdfc_atm.withdraw(90))
#     print(hdfc_atm.withdraw(500000))
#
#     icici_atm = ATM("sath")
