"""
Manage trained things
"""

from utility.exception import AlreadyKnownError


class Info:
    """
    Manage information about objects
    """
    bool_str_mapper = {
        True: "",
        False: "not"
    }

    def __init__(self, _bool, name, value):
        self.bool = _bool
        self.name = name
        self.value = value

    def __repr__(self):
        return f"<Info {self.name} is {self.bool_str_mapper[self.bool]} {self.value}>"


class Thing:
    """
    Manage learned objects
    Apple, Person, ... Just 'Things'
    """

    def __init__(self, name=None):
        self.name = name
        self.__info = ["name"]

    def __repr__(self):
        return f"<Thing {self.name}>"

    def learn_info(self, name, value, _bool=True, force=False):
        try:
            # check already know
            assert getattr(self, name) is not None
        except (AttributeError, AssertionError):
            self.__add_new_info(name, value, _bool)
        else:
            # if already know
            # check force learning option
            if force is True:
                self.__add_new_info(name, value, _bool)
            else:
                # raise AlreadyKnowError
                raise AlreadyKnownError("This information is already known.")

    def __add_new_info(self, name, value, _bool):
        setattr(self, name, Info(_bool, name, value))
        self.__info.append(name)

    @property
    def info_list(self):
        return self.__info


class Brain:
    """
    Manage knowledge that learned.
    """

    def __init__(self, username):
        # Name for user identification.
        self.username = username
        self.__learned_list = list()

    def __repr__(self):
        return f"<Brain {self.username}>"

    def print_my_knowledge(self):
        print("\n")
        print("------------Brain Status------------")
        for know in self.__learned_list:
            if type(know) == Info:
                print(f"[Info] {know.name} is {know.value}. positive: {know.bool}")
            elif type(know) == Thing:
                pass

        print("\n\n")

    def remember_things(self, name):
        for learned_thing in self.__learned_list:
            if learned_thing.name == name:
                return learned_thing
        else:
            return None

    def learn(self, name, attr=None, value=None, _bool=None, force=False):
        if attr is None:  # Just Add things
            self._learn_thing(name, force=force)
        else:
            self._learn_info(name, attr, value, _bool)

    def _learn_thing(self, name, force=False):
        try:
            # check already know
            assert self.remember_things(name) is not None
        except AssertionError:
            self.__add_new_thing(name)
        else:
            # if already know
            # check force learning option
            if force is True:
                self.__add_new_thing(name)
            else:
                # raise AlreadyKnowError
                raise AlreadyKnownError(f"{name} is already known.")

    def _learn_info(self, name, attr, value, _bool):
        known_thing = self.remember_things(name)

        if known_thing is None:
            self.__add_new_thing(name)
            known_thing = self.thing_just_before

        known_thing.learn_info(attr, value, _bool)

        self.__add_new_info(name, value, _bool)

    def __add_new_info(self, name, value, _bool):
        self.__learned_list.append(Info(_bool, name, value))

    def __add_new_thing(self, name):
        self.__learned_list.append(Thing(name))

    @property
    def thing_just_before(self):
        return self.__learned_list[-1]
