class myClass:
    def __init__(self):
        pass

    def foo(self,value:int) -> int:
        return value

myInstance = myClass()

assert myInstance.foo(value=3) == 1
