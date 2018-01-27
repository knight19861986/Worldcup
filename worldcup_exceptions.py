class WorldCupException(Exception):
    def __init__(self, value):
        self.infomation = value

    def __str__(self):
        return repr(self.infomation)


class IllegalConfederationException(WorldCupException):
    def __init__(self, value):
        self.infomation = value


class IllegalPotException(WorldCupException):
    def __init__(self, value):
        self.infomation = value


class NonePotException(WorldCupException):
    def __init__(self, value):
        self.infomation = value


class HasBeenSelectedException(WorldCupException):
    def __init__(self, value):
        self.infomation = value
