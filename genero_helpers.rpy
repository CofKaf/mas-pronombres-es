init -10 python:
    def gen(f="a", m="o", x="e"):
        if getattr(persistent, 'gender', 'M') == "F":
            return f
        elif getattr(persistent, 'gender', 'M') == "M":
            return m
        return x

    def w(f, m, x="e"):
        if getattr(persistent, 'gender', 'M') == "F":
            return f
        elif getattr(persistent, 'gender', 'M') == "M":
            return m
        return x