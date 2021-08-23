class MyClass:
    def __init__(self):
        self.text = self.getstring()
        self.printstring()

    def getstring(self):
        x = input("enter ur desired text and see what happens then:")
        return x

    def printstring(self):
        print(self.text)


mc = MyClass()
mc.getstring()
mc.printstring()



