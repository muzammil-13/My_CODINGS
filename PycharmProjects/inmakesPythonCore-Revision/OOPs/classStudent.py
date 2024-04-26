class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getdetails(self):
        self.name = input("Enter your name:")
        self.mark = int(input("Enter your mark:"))

    def putdetails(self):
        print(self.name, self.mark)


obj = Student('', '')
obj.getdetails()
obj.putdetails()
