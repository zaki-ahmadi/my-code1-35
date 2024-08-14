# (1)
class FileManager:
    def __init__(self,name):
        self.name = name

    def open_file_read(self):
        print('file opened to read')
        o_r = open('abc.txt', "r")
        print(o_r.read())
        

    def open_file_write(self):
        print('file opened to write')

        o_w = open('abcd.txt', "w")
        print(o_w.write('hello world '))
        print(o_w.write('new line'))
        
        o_w.close
        

a = FileManager('file to read and write')
a.open_file_read()
a.open_file_write()


print('_________________________________________________________')
# (2)

class Log:
    def __init__(self ,file_t):
        self.file_t = file_t

    def write_error(self ,error_message):
        with open('error.txt', 'a') as file:
            file.write(f'Error : {error_message}\n')
            print('in the file error was sent!!!')


log = Log('error.txt')
log.write_error('this is an error masege')

print('_________________________________________________________')
# (3)


class Config:
    def read(self):
        with open("configuration setings.txt","r") as f:
            print(f.__dir__())

    def access_dir(self):
        with open("configuration setings.txt","r+") as f:
            print(f.__dir__())

label=Config()
label.access_dir()



print('_____________________________________________________________')


# (4)

list = ["ali","abbas","sara","aziz"]
class Database:
    global list

    def queries(self,name):
        try:
            for i in list:
                if i == n:
                    print(f"your name is{name}")

        except:
            print("connection fails")

jawad = Database()
jawad.queries("jawad")

print('___________________________________________________________________')
# (5)


class Report:
    try:
        def generate_data(self):
            with open("dat.txt","r") as f:
                print(f.readlines())


    except FileNotFoundError :
         print("file does not exist or can not read")

new=Report()
new.generate_data()
