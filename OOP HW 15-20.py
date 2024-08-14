# (1)

from typing import Any


class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []


    def add_book(self,book):
        self.books.append(book)
        print(f'this book <<{book.title}>> added to library.')

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f'this <<{book.title}>> removed from library.')
        else:
            print('this book is not here.')
    
    def show_all_books(self):
        if self.books:
            print('the all of books in library:')
            print()
            for book in self.books:
                print(f'name of book: {book.title}, author :{book.author}')
        else:
                print('library is empaty.')
                
Library1 = Library('Kabul University Library')
book1 = Book('Afghanistan', 'Mohammad')
book2 = Book('Kabul', 'Ali Mohammad')
Library1.add_book(book1)
Library1.add_book(book2)
print()
Library1.show_all_books()

print('____________________________________________________')


# (2)
class stu:
    def __init__(self,name):
        self.name = name
        
class School:
    def __init__(self,name):
        self.name = name
        self.students = []


    def add(self,student):
        self.students.append(student)
        print(f'{student.name} added to school.')
    
    def rem(self,student):
        if student in self.students:
            self.students.remove(student)
            print(f'{student.name} removed from scholl.')

        else:
            print(f'{student} is not in our school.')


sch = School('Abdul-rahim-e-shahid')
stu1 = stu('ali')
sch.add(stu1)
sch.rem(stu1)


print('____________________________________________________')

# (3)
class Members:
    def __init__(self, name_menber):
        self.name_menber = name_menber


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_mem(self, member):
        self.members.append(member)
        print(f'{member.name_menber} added to team')

    def remove_mem(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f'{member.name_menber} removed from team')
        else:
            print(f'{member} is not in this team')


team_football = Team('ITF')
mem_1 = Members('jawid')
team_football.add_mem(mem_1)
mem_2 = Members('zaki')
team_football.add_mem(mem_2)
mem_3 = Members('ali')
team_football.add_mem(mem_3)
mem_4 = Members('ahmad')
team_football.add_mem(mem_4)
team_football.remove_mem(mem_3)


print('____________________________________________________')

# (4)


class Employee:
    def __init__(self,name_e):
        self.name_e = name_e



class Factori:
    def __init__(self,name):
        self.name = name
        self.employees = []


    def a_d(self,employee):
        self.employees.append(employee)
        print(f'{employee.name_e} added to factori ' )

    def r_m(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f'{employee.name_e} removed from factori ' )
        else:
            print(f'he/she is not in this <<{self.name}>> Factori ')


fact_099 = Factori('Tesla')
emp_099 = Employee('zaki')
fact_099.a_d(emp_099)
fact_099.r_m(emp_099)

print('____________________________________________________')

# (5)



class Animal:
    def __init__(self,name_a):
        self.name_a = name_a



class Zoo:
    def __init__(self,name):
        self.name = name
        self.animals = []


    def a_a(self,animal):
        self.animals.append(animal)
        print(f'{animal.name_a} added to zoo ' )

    def r_a(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f'{animal.name_a} removed from zoo ' )
        else:
            print(f'it is not in this <<{self.name}>> zoo ')

zoo = Zoo('international zoo of USA')
ani = Animal('dog')
zoo.a_a(ani)