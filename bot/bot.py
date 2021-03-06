from random import choice

from utility.exception import AnalysisError
from .knowledge import Brain
from .parser import Analyzer
from .expression import agreement, sympathy


class Bot:
    def __init__(self, name):
        self.name = name
        self.brain = Brain(self.name)

    def __repr__(self):
        return f"<Bot {self.name}>"

    @staticmethod
    def make_response_sentence(expression_module, *args):
        expression_list = expression_module.expression
        if len(args) is 0:
            exp = choice(expression_list)

        else:
            exp = (choice(expression_list) % args)
        return exp

    def get_response(self, talk):
        # print(f"[Bot LOG] Start Analyze {talk}")

        try:
            anal = Analyzer(talk)
        except AnalysisError:
            # if there is no designator
            # Just return sympathy expression
            # print(f"[Bot LOG] Can't Analysis \"{talk}\"")
            resp = Bot.make_response_sentence(sympathy)
        else:
            self.brain.learn(anal.name, anal.attr, anal.mean, anal.bool_type)

            resp = Bot.make_response_sentence(agreement, anal.name, anal.mean)

        # print(f"[Bot LOG] Make response.")
        return resp
