from oop import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self, a, b):
        Calculator.__init__(self, a, b)

        #def __init__(self):
        #Calculator.__init__(self, 2, 6)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())