#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    signs = '-+*/'
    for c in signs:
        if c == '-':
            fun = calc.sub
        elif c == '+':
            fun = calc.add
        elif c == '*':
            fun = calc.mul
        elif c == '/':
            fun = calc.div
        print("{} {} {} = {}".format(a, c, b, fun(a, b)))
