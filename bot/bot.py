from .knowledge import Brain
from .parser import Analyser


class Bot:
    def __init__(self, name):
        self.name = name
        self.brain = Brain(self.name)

    def __repr__(self):
        return f"<Bot {self.name}>"

    def get_response(self, talk):
        print(f"Start Analyze {talk}")
        anal = Analyser(talk)

        known = self.brain.remember_things(anal.name)

        if known is None:  # if we don't know
            print(f"Get New Thing. {anal.name}")
            # learn(self, name, value=None, _bool=None, force=False)
            self.brain.learn(anal.name, anal.mean, anal.bool_type)

        else:  # if we already know
            print(f"Get Already Known Thing. {anal.name}")
            known.learn_info(anal.name, anal.mean, anal.bool_type)

        return talk
