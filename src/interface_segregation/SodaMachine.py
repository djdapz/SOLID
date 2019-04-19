from interface_segregation.DrinkMachine import DrinkMachine


class SodaMachine(DrinkMachine):

    @staticmethod
    def pour():
        return "COLA"
