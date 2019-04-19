from liskov.Worker import Worker


class HumanWorker(Worker):

    @staticmethod
    def eat(food):
        if food == "broccoli":
            return 'YUK! I DONT LIKE VEGGIES'
        else:
            return 'YUM! THAT WAS DELICIOUS'

    @staticmethod
    def work():
        return "YAY WORK"

