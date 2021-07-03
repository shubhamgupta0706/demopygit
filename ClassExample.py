class Person:
    def __init__(self):
        print('Inside init A')

    '''def __init__(self, x):
        print('Inside Argumented and the value of given passed argu(ment is: ', x)'''

    def talk(self):
        print('Hey there!, my name is '+self.name)


class Employee(Person):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print('Inside Init B')

    def works(self):
        print("I'm working...")


tarun = Employee('Tarun Dubey')
tarun.talk()
tarun.works()


