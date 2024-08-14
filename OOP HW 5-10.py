print('The first question ')
# (1)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'SPEAK SPEAK SPEAK')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + 'OW OW OW OW')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + 'MIOW MIOW MIOW')


animal1 = Animal('an animal speak\'s : ')
animal1.speak()

dog1 = Dog('dog name is max and speak like this : ')
dog1.speak()

cat1 = Cat('cat name is bilo and speak like this : ')
cat1.speak()

print('The second question ')
# (2)

class Shapes:
    def __init__(self):
        pass

class Area_of_Square(Shapes):
    def __init__(self, tool , arz):
        self.tool = tool
        self.arz = arz

    def area(self):
        print(self.tool * self.arz)



class Area_of_Triangle(Shapes):
    def __init__(self,qaidah, ertifa):
        self.qaidah = qaidah
        self.ertifa = ertifa



    def area(self):
        print(0.5 * self.qaidah * self.ertifa)



squ = Area_of_Square(4 ,4)
squ.area()
tri = Area_of_Triangle(2 ,4)
tri.area()


print('The theard question ')
# (3)

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary



class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department



manager1 = Manager('adulkhaliq', 10000 , 'information technologe')
print(manager1.name)
print(manager1.salary)
print(manager1.department)


print('The fuorth question ')
# (4)

class Vehicle:
    def __init__(self,name):
        self.name = name

    def drive(self):
         print('vehicle drive drive !!! 🛞🛞🛞')

class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
         print(f'{self.name} ride ride !!! 🚲🚲🚲' )
    
class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
         print(f'{self.name} drive drive !!! 🚜🚜🚜' )
    
bike1 = Bike('ali\'s bike')
bike1.drive()
truck1 = Truck('ahmad\'s truck')
truck1.drive()


print('The fifth question ')
# (5)

class Bird:
    def __init__(self,name_of_bird):
        self.name_of_bird = name_of_bird


    def fly(self):
        print(f'{self.name_of_bird} flying ')
class Eagle(Bird):
    def __init__(self, name_of_bird):
        super().__init__(name_of_bird)


    def fly(self):
        print(f'{self.name_of_bird} can fly !!! ')

class Penguin(Bird):
    def __init__(self, name_of_bird):
        super().__init__(name_of_bird)

    
    def fly(self):
        print(f'{self.name_of_bird} can not fly !!! ')


eagle1 = Eagle('Eagle🦅🦅🦅')
eagle1.fly()
Penguin1 = Penguin('Penguin🐧🐧🐧')
Penguin1.fly()