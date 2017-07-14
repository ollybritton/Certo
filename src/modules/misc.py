# ---
# misc.py
# Functions that don't really have a place anywhere else.
# ---

def capital_case(string):
    string = string.split(" ")

    for i in range(len(string)):
        s = string[i]

        string[i] = s[0].upper() + "".join(list(s)[1:])

    return " ".join(string)
