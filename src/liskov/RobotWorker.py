from liskov.Worker import Worker


class RobotWorker(Worker):

    @staticmethod
    def eat(junk):
        raise NotImplementedError()

    @staticmethod
    def work():
        return "BEE BOP WORK"

