import abc


class MakerMachine(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def make():
        pass
