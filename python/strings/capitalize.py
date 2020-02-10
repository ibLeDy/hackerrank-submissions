def solve(s):
    if s.endswith("3g"):
        return s[:-2].title() + "3g"

    return s.title()
