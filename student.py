class Student:
    #ATTRIBUTES
    def __init__(self, name, age, hobby, book=1, grade=0.5 ):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.book = book
        self.grade = grade

    #METHODS
    def introduce_self(self):
        return f'Hello, my name is {self.name}'

    def add_book(self):
        self.book += 1
        return self.book
    

student1 = Student('vincent', 16, 'soccer', 3, 9.8)
student2 = Student('vannes', 17, 'basketball', 2, 3.4)

addbook_student1 = student1.add_book()
print(addbook_student1)
