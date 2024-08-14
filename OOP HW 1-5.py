# from math import pi
# # oop home work 

# # (1)
# class Person :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


# ali = Person('ali', 20)



# # (2)
# class Person1 :
#   def __init__(self,name,age):
#       self.name = name
#       self.age = age
    

#   def greet(self):
#       print('Hello Wellcome Mr:' + self.name)

# first_person1 = Person1('Ahsan', 14) 
# first_person1.greet()



# # (3)
# class Car:
#     def __init__(self,model,made,year):
#         self.model = model
#         self.make = made
#         self.year = year


# car1 = Car('Benz','made by USA', 2020)

# print(car1.make)
# print(car1.model)
# print(car1.year)


# # (4)
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         a_a = pi * (self.radius ** 2)
#         print(a_a)


# cri1 = Circle(5)
# cri1.area()
    
# # (5)

# class A_P:

#     def __init__(self, tool, arz):
#         self.tool = tool
#         self.arz = arz

#     def area(self):
#         a_t = self.tool * self.arz
#         print(a_t)

#     def enviroment(self):
#         p_t = (self.tool * 2) + (self.arz * 2)
#         print(p_t)


# ap1 = A_P(5, 4)
# ap1.area()
# ap1.enviroment()





# class Employee:
#     def __init__(self,name_e):
#         self.name_e = name_e



# class Factori:
#     def __init__(self,name):
#         self.name = name
#         self.employees = []


#     def a_d(self,employee):
#         self.employees.append(employee)
#         print(f'{employee.name_e} added to factori ' )

#     def r_m(self,employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#             print(f'{employee.name_e} removed from factori ' )
#         else:
#             print(f'he/she is not in this <<{self.name}>> Factori ')


# fact_099 = Factori('Tesla')
# emp_099 = Employee('zaki')
# fact_099.a_d(emp_099)
# fact_099.r_m(emp_099)








class car:
    def __init__(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year

    def show(self):
        print(f'model : {self.model} \nmake : {self.make} \nyear : {self.year}' )


car1 = car('benz' , 'USA' , 2020)
car1.show()

print('-----------------------------------')

# (7)
class shape:
    def area(self):
        pass


class square(shape):
    def __init__(self,tool,arz):
        self.tool = tool
        self.arz = arz

    def area(self):
        a = self.tool * self.arz
        print(a)

class tringle(shape):
    def __init__(self,base,hight):
        self.base = base
        self.hight = hight

    def area(self):
        b = 0.5 * self.hight *self.base
        print(b)


s1 = square(4,4)
s1.area()

t1 = tringle(3,5)
t1.area()

print('-----------------------------------')

class Employee:
    def __init__(self,name_e):
        self.name_e = name_e

class Factori:
    def __init__(self,name):
        self.name = name
        self.employees = []


    def add(self,employee):
        self.employees.append(employee)
        print(f'{employee.name_e} added to factori')

    def remove(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f'{employee.name_e} removed from factori ')

        else:
            print('error')

f = Factori('tesla')
e1 = Employee('ahmad')

f.add(e1)
f.remove(e1)