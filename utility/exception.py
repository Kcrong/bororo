# original at python3 - contextlib.suppress


class ignore:
    def __init__(self, *exceptions, error_message=None):
        self._exceptions = exceptions
        self.error_message = error_message

    def __enter__(self):
        """
        When execute `with ignore(Exception)`
        Override, And Do anything!
        """
        if self.error_message is None:
            pass
        else:
            print(self.error_message)

    def __exit__(self, exception_type, *_):
        """
        :param exception_type: Exception type that you catch
        :param _: Unused param. (to me..)
        :return: Boolean
        """
        return exception_type is not None and issubclass(exception_type, self._exceptions)


class InvalidRuleException(Exception):
    pass


class CompleteEvolution(Exception):
    pass
