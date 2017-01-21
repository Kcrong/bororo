from random import choice

from utility.exception import AnalysisError
from .knowledge import Brain
from .parser import Analyser
from .expression import agreement, ask, sympathy


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
        print(f"Start Analyze {talk}")

        try:
            anal = Analyser(talk)
        except AnalysisError:
            # if there is no designator
            # Just return sympathy expression
            resp = Bot.make_response_sentence(sympathy)
        else:
            # else, there is designator
            known = self.brain.remember_things(anal.name)

            if known is None:  # if we don't know
                print(f"Get New Thing. {anal.name}")
                # learn(self, name, value=None, _bool=None, force=False)
                self.brain.learn(anal.name, anal.mean, anal.bool_type)

            else:  # if we already know
                print(f"Get Already Known Thing. {anal.name}")
                known.learn_info(anal.name, anal.mean, anal.bool_type)

            resp = Bot.make_response_sentence(agreement, anal.name, anal.mean)

        return resp
