class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduction(self):
        return f'My name is {self.name},\nI am {self.age} years old.'



john = Student('john', 15, 'A+')
bill = Student('bill', 16, 'B')

intro = john.introduction()
print (intro)