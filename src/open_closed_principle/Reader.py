import abc


class Reader(abc.ABC):

    @abc.abstractmethod
    def read(self):
        pass

