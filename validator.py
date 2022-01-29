import re


def check_valid_email(_email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.fullmatch(regex, _email):
        return True
    else:
        return False
