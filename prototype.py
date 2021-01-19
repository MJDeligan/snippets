class Base():
    def __init__(self, value):
        self.value = value
    
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
        super().__init__(value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value