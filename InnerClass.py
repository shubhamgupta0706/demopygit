class Student:
    school = 'Gyan Ganga'

    def __init__(self, name, age, rollno):
        self.name=name
        self.age=age
        self.rollno = rollno
        self.lap=self.Laptop()

    def show(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Roll No:', self.rollno)
        # print('Laptop:', self.lap.brand, self.lap.CPU, self.lap.ram)
        self.lap.show()  # Calling inner class object inside outer class function

    class Laptop:

        def __init__(self):
            self.brand = 'Asus Vivobook'
            self.CPU = 'i5 11th Gen'
            self.ram = '8 GB'

        def show(self):
            print('Laptop:', self.brand, self.CPU, self.ram)


s1 = Student('Shubham', 23, '0206CS151154')
s1.show()

# Creating object of inner class outside of outer class
lap1 = Student.Laptop()
lap1.show()