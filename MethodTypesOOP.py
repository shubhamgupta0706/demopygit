class Student:
    school = 'Gyan Ganga'

    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def get_avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('Hello!, Welcome to', Student.getSchool())


s1 = Student(58, 97, 54)
print(s1.get_avg())
Student.info()