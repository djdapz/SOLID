from interface_segregation.MakerMachine import MakerMachine


class RiceMaker(MakerMachine):

    @staticmethod
    def make():
        return "RICE"
