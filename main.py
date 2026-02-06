class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"Ismi: {self.name}, Yoshi: {self.age}, Bahosi: {self.grade}")


student1 = Student("Ali", 12, 5)
student1.info()
