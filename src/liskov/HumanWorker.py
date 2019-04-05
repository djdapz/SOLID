from liskov.Worker import Worker


class HumanWorker(Worker):

    @staticmethod
    def work():
        return "YAY WORK"

