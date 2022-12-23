from cmath import exp
from http import server


class ConnectionEror(Exception):
    pass


class NoServerAvailableError(Exception):
    pass

class AccountNotFoundError(Exception):
    pass    


class NotLoggedInError(Exception):
    pass