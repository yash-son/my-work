'''
•Objects represent real-world entities, and
classes act as blueprints for creating objects.
'''

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'Name: {self.name},Age: {self.age}')

s1=student('yash',34)
s1.display()

class partyanimal:
    def __init__(self):
        self.x=0
    def party(self):
        self.x= self.x +1
        print(f"The value is",self.x)
s=partyanimal()
s.party()
s.party()
s.party()

class car:
    def __init__(self,make,model,year):
        self.year=year
        self.model=model
        self.make=make
    def start(self):
        print("the car is starting ")
    def stop(self):
        print('the car is stopping')
car1=car("Toyota","W",2020)
car1.start()
car1.stop()   

class Gradebook:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def add_grades(self):
        total=0
        for i in self.grade:
            total+=i
        return total
    def average_grade(self):
        total=self.add_grades()
        avg=total/len(self.grade)
        print("the avg is ",avg)
s1=Gradebook('Yash',[1,2,3])
s1.average_grade()



