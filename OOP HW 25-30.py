# (1)
class Ticket:
    def __init__(self,movie_name,seat_num,price):
        self.movie_name = movie_name
        self.seat_num = seat_num
        self.price = price

    def show_details(self):
        print(f'movie_name : {self.movie_name} \nseat_num : {self.seat_num},\nprice : {self.price} ')
    def takhfif(self,amount):
        if 0 < amount < self.price:
            self.price -= amount
            print(f'{amount} afghani is you takhfif.')

        else:
            print('an error')


ahmad = Ticket('love' , 99 , 350)

ahmad.show_details()

ahmad.takhfif(50)

ahmad.show_details()
            
# (2)
print('____________________________________________')

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f'{name} added to items ')

    def rem_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f'{name} is removed.')
        else:
            print(f'{name} is not in items ')

    def show_item(self):
        if not self.items:
            print('the items is emapaty .')
        else:
            for name, price in self.items.items():
                print(f'name : {name} , price : {price}')


sho = ShoppingCart()
sho.add_item('milk', 25)
sho.add_item('wather', 10)
sho.add_item('egg', 10)
sho.show_item()
print('after of the remove')
sho.rem_item('milk')
sho.show_item()

# (3)
print('____________________________________________')
class Reatsurant :
    def __init__(self,name):
        self.name = name
        self.menu = []

    def add_to_menu(self,name_food):
        self.menu.append(name_food)
        print(f'{name_food} added to the menu')

    def remove_from_menu(self,name_food):
        if name_food in self.menu:
            self.menu.remove(name_food)
            print(f'{name_food} removed from the menu')

    def display_menu(self):
        print('the menu of the Reatsurant')
        for food in self.menu:
            print(f'food : {food}')



abc = Reatsurant('Barg Continital')
abc.add_to_menu('Palaw')
abc.add_to_menu('Shorba')
abc.add_to_menu('Kabab')
abc.remove_from_menu('Palaw')
abc.display_menu()

print('____________________________________________')
# (4)

class Flight:
    def __init__(self,flight_num,destination,):
        self.flight_num = flight_num
        self.destination = destination
        self.passengers = []

    def add_passenger(self,person):
        self.passengers.append(person)
        print(f'{person} added to this Flight going to {self.destination}.')
        print()
    def remove_passengers(self,person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person} removed from this Flight to the going {self.destination}')
            print()
    def show_all_passengers(self):
        for i in self.passengers:
            print(f'name of passengers : {i}')
        print()


flight404 = Flight( 404 , 'Kabul')
flight404.add_passenger('ali')
flight404.add_passenger('zaki')
flight404.add_passenger('abdullah')
flight404.add_passenger('haji')
flight404.show_all_passengers()
flight404.remove_passengers('haji')
flight404.show_all_passengers()



print('____________________________________________')

# (5)

class Hotel:
    def __int__(self, name, room_numbers):
        self.name = name
        self.room_numbers
        self.rooms = {num: False for num in room_numbers}

    def book(self, room_number):
        if not self.rooms[room_number]:
            self.rooms[room_number] = True
            return f'{room_number} is booked'
        return f'{room_number} before you was booked'

    def check_out(self,room_number):
        if self.rooms[room_number]:
            self.rooms[room_number] = False
            return f'{room_number} is check out'
        return f'{room_number} was check outed'

hotel1 = Hotel('kabul' , [1,2,3])
print(hotel1.book(1))
print(hotel1.check_out(3))


