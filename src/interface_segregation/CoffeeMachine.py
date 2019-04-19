from interface_segregation.DrinkMachine import DrinkMachine
from interface_segregation.MakerMachine import MakerMachine


class CoffeeMachine(DrinkMachine, MakerMachine):
    @staticmethod
    def pour():
        return "COFFEE"

    @staticmethod
    def make():
        return "COFFEE"
