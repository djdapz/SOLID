from liskov.Worker import Worker


class RobotWorker(Worker):

    @staticmethod
    def work():
        return "BEE BOP WORK"

