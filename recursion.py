def rec(n):
    r = n % 10
    d = n / 10

    if d == 0:
        return r
    
    return r + rec( n/10)

def rev(string):
    if len(string) <= 1:
        return string
    
    return string[1:] + string[0]

def pemute(s):
    out = []

    if len(s) == 1:
        out = [s]

    for i, letter in enumerate(s):

        for per in pemute(s[:i] + s[i + 1:]):
            out += [letter + per]

    return out
