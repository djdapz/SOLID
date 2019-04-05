import abc


class Worker(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def work():
        pass

