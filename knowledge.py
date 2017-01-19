"""
Manage trained things
"""


class KnownError(Exception):
    pass


class Info:
    bool_str_mapper = {
        True: "",
        False: "not"
    }

    def __init__(self, bool, name, value):
        self.bool = bool
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

    def learn_info(self, name, value, force=False):
        try:
            # 기존에 알고있던 정보
            assert getattr(self, name) is not None
        except (AttributeError, AssertionError):
            self.__add_new_info(name, value)
        else:
            # 이미 알고있던 정보일 경우
            # 강제 기억
            if force is True:
                self.__add_new_info(name, value)
            else:
                raise KnownError("This information is already known.")

    def __add_new_info(self, name, value):
        setattr(self, name, value)
        self.__info.append(name)

    @property
    def info_list(self):
        return self.__info
