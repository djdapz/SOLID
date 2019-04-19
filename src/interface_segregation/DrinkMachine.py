import abc


class DrinkMachine(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def pour():
        pass
