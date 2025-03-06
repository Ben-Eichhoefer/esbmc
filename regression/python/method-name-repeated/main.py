class FirstClass:
    def __init__(self):
        pass

    def add(self, val1:int, val2:int) -> int:
        return val1 + val2

class SecondClass:
    def __init__(self):
        pass

    def add(self, num1:int, num2:int) -> int:
        return num1 + num2 + 1


summer = FirstClass()

assert summer.add(val1=1,val2=2) == 3
assert summer.add(1,2) == 3