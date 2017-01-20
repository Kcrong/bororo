from .knowledge import Brain
from utility.logging import Logging


class Bot:
    def __init__(self, name):
        self.name = name
        self.brain = Brain(self.name)
        self.logger = Logging(self.name)

    def __repr__(self):
        return f"<Bot {self.name}>"

    def get_response(self, talk):
        return talk
