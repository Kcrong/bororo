"""
Manage trained things
"""


class KnownError(Exception):
    pass


class Thing:
    def __init__(self):
        self.name = None

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
