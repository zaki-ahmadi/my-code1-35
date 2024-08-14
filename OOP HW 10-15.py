# (1)
class Account:

    def __init__(self, in_money=0):
        self.__in_money = in_money

    def input_money(self, amount):
        if amount > 0:
            self.__in_money += amount
            print(f'{amount} money inputed in the Account ')

        else:
            print('an Error ❌❌❌')

    def output_money(self, amount):
        if 0 < amount <= self.__in_money:
            self.__in_money -= amount
            print(f'{amount} money outed from the Account ')
        else:
            print('an Erronr ❌❌❌')

    def allin_the_account_money(self):
        print(self.__in_money)


Account1 = Account(500)

Account1.input_money(500)

Account1.output_money(300)

Account1.allin_the_account_money()




# (2)
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages


book1 = Book('Programing', 'ali ahmadi', 678)
print(book1.get_title())

book1.set_pages(900)
print(book1.get_pages())

print(book1.get_author())


# (3)
class Laptop:
    def __init__(self, model, brand, price) :
        self.__model = model
        self.__brand = brand
        self.__price = price

    def takhfif(self, takhfif_laptop):
        if 0 < takhfif_laptop < self.__price:
            self.__price -= takhfif_laptop
        else:
            print('an Error ')


    def show_model_brand_price(self):
        print(f'the laptop model is {self.__model}.')
        print()
        print(f'the laptop brand is {self.__brand}.')
        print()
        print(f'the laptop price is {self.__price}.')
        print()



Laptop1 = Laptop('dell_7400', 'Dell', 18000)

Laptop1.show_model_brand_price()


print('After of the takhfif ⬇️  ⬇️  ⬇️')
print()
Laptop1.takhfif(3000)

Laptop1.show_model_brand_price()


# (4)
class BankAccount:
    def __init__(self, account_num, blance=0):
        self.__account_num = account_num
        self.__blance = blance


    def in_money(self,amount):
        if amount > 0 : 
            self.__blance += amount
            print(f'You {amount} (Afghni) inputed in your bank_account')
        else:
            print('an Error')

    def out_money(self,amount):
        if 0 < amount <= self.__blance:
            self.__blance -= amount
            print(f'You {amount} (Afghni) was outputed from your bank_account ')
        else:
            print('an Error')


    def show_blance(self):
        print(f'Your blancce is : {self.__blance} (Afghni)')

ali_acc = BankAccount(56565656,7800)

ali_acc.show_blance()

ali_acc.in_money(200)

ali_acc.out_money(3000)

ali_acc.show_blance()


# (5)


class Student:
    def __init__(self,name,grade,age):
        self.__name = name
        self.__grade = grade
        self.__age = age

    def get_name(self):
        print(self.__name)
        
    def get_grade(self):
        print(self.__grade)

    def get_age(self):
        print(self.__age)

    def set_name_grade_age(self,name,grade,age):
        self.__name = name 
        self.__grade = grade
        self.__age = age

    def show_details_of_students(self):
        print(f'name : {self.__name} \ngrade : {self.__grade} \nage : {self.__age}')



ali = Student('ali' , 'first' , 20)
print('befor changing the details of student.\n⬇️')
ali.show_details_of_students()
ali.set_name_grade_age('ali' , 'second' , '21')
print('after changing the details of student.\n⬇️')
ali.show_details_of_students()
