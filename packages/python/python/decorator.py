from functools import partial

def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

# def square(base):
#     return power(base, 2)

# def cube(base):
#     return power(base, 3)

def power(base, exponent):
    return base ** exponent


cube = partial(power, exponent=3)

square = partial(power, exponent=2)
square(5)