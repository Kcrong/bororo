"""
Manage trained things
"""


class AlreadyKnowError(Exception):
    pass


class Info:
    bool_str_mapper = {
        True: "",
        False: "not"
    }

    def __init__(self, _bool, name, value):
        self.bool = _bool
        self.name = name
        self.value = value

    def __repr__(self):
        return f"<Info {self.name} is {self.bool_str_mapper[self.bool]} {self.value}"


class Thing:
    def __init__(self):
        self.name = None
        self.__info = ["name"]

    def __repr__(self):
        return f"<Thing {self.name}"

    def learn_info(self, name, value, _bool, force=False):
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
                raise AlreadyKnowError("This information is already known.")

    def __add_new_info(self, name, value, _bool):
        setattr(self, name, Info(_bool, name, value))
        self.__info.append(name)

    @property
    def info_list(self):
        return self.__info
