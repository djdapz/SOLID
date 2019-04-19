import abc


class Worker(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def work():
        pass

    @staticmethod
    @abc.abstractmethod
    def eat(food):
        pass
