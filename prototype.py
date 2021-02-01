# From just == and < we are usually able
# to deduce the behaviour of the other
# operators

# note that the Base class implements
# no operator directly, but instead
# defines them all dependent on each other

# we can thus inherit from the base
# class and implement any number of
# comparison operators as long
# as we imlpement either == or != and
# < or > we will be able to use them all

# while it might seem like this is standard
# behaviour in python, try using Derived
# without inheriting from Base
# while implementing == and < does also
# provide implementations for != and >
# trying <= and >= will result in error
# because they are not defined
class Base():
    def __eq__(self, other):
        return not (self != other)

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return not (self < other) and not (self == other)

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not (self > other) and not (self == other)

    def __le__(self, other):
        return self < other or self == other


class Derived(Base):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value
