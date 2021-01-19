""" 
Curry takes any function with a determined amount of arguments
and curries it, meaning it will be turned into a function that
consumes only 1 argument and returns another function which also
consumes only 1 argument until we have a function for each
argument. The final function returns just the result of applying
the arguments of all previous functions to inputfunction
"""
def curry(f, args=[]):
    return f(*args) if len(args) == f.__code__.co_argcount else lambda x: curry(f, args=args+[x])

# curry can also be used as a decorator immediately turning the function into a curried version
@curry
def add(a, b):
    return a + b


# takes a function
# returns a function which takes a list as a parameter and returns a
# generator where each element has the function applied to it
def partial_map(f):
    return lambda xs: (f(x) for x in xs)
