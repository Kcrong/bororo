from .knowledge import Brain
from .parser import Analyser


class Bot:
    def __init__(self, name):
        self.name = name
        self.brain = Brain(self.name)

    def __repr__(self):
        return f"<Bot {self.name}>"

    def get_response(self, talk):
        return talk
