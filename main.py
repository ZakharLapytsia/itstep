class Human:
    height = 170

    def __init__(self):
        self.height = 150
class Student(Human):
    def __init__(self):
        print(self.height)
        super().__init__()
        print(self.height)
        print(super().height)

class Worker(Human):
    pass
nick = Student()
ann = Worker()