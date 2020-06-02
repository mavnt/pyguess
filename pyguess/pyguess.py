import datetime
import json
import re


# https://stackoverflow.com/a/54393495
def pyguess(s: str, cast=True):
    s = s.strip()
    if re.match("[0-9]+\.[0-9]+", s):
        return float(s) if cast else float
    elif re.match("[0-9]+", s):
        return int(s) if cast else int
    elif re.match("[0-9]{4}-[0-9]{2}-[0-9]{2}", s):  # TODO
        y, m, d = map(lambda x: int(x), s.split("-"))
        return datetime.date(y, m, d) if cast else datetime.date
    elif s.lower() == "true":
        return True if cast else bool
    elif s.lower() == "false":
        return False if cast else bool
    elif s == "None":
        return None if cast else type(None)
    else:
        try:
            d = json.loads(s)
            return d if cast else dict
        except:
            pass
        return str(s) if cast else str
