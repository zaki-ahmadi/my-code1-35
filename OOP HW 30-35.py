# سوالات پایتون از ۳۶ تا ۴۰  یا از ۳۱ تا ۳۵ 

# (1)
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("CounterApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
total_m= 1000000
label1 =ttk.Label(window,text="Your current account equal :",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
global_var =1000000
label2 =ttk.Label(window,text= global_var ,font="arial 12",background="green")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your amount...?')
def d_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var - new_m
    label2['text']= global_var

def i_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var + new_m
    label2['text']= global_var

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)
button1 =ttk.Button(window, text="Decrement button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")
button2 =ttk.Button(window, text="Increment button", width=22,command=i_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()


print('__________________________________________________________________')

# (2)

window = tk.Tk()
window.title("ToDoApp")
window.geometry("700x400")
window.config(bg="orange")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)

label1 =ttk.Label(window,text="Tasks : Teacher, Docter, ",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
list_task= ["Manager,","Officer,","Minister"]
label2 =ttk.Label(window,text= list_task ,font="arial 12",background="gray")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your task...?')

def d_button():
    global list_task
    new_m =str( entry_var.get())
    for i in list_task:
        if i == new_m:
            list_task.remove(i)
    label2['text'] = list_task

def a_button():
    global list_task
    new_m =str( entry_var.get())
    list_task.append(new_m)
    label2['text']= list_task

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)

button1 =ttk.Button(window, text="Delete button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")

button2 =ttk.Button(window, text="Add button", width=22,command=a_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()




print('__________________________________________________________________')
# (3)


calculator = ""
def add_to_calculation(symbol):
    global calculator
    calculator += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculator)
def evaluate_calculation():
    global calculator
    try:
        calculator = str(eval(calculator))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculator)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculator
    calculator =""
    text_result.delete(1.0, "end")

window=tk.Tk()
window.title("calculator")
window.geometry("300x300")
window.resizable(False,False)
text_result = tk.Text(window,height=2, width = 16, font =("Arial", 24))
text_result.grid(columnspan = 5)
btn_1 = tk.Button(window, text ="1", command = lambda: add_to_calculation(1),width = 5, font = ("Arial",14))
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(window, text ="2", command = lambda: add_to_calculation(2),width = 5, font = ("Arial",14))
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(window, text ="3", command = lambda: add_to_calculation(3),width = 5, font = ("Arial",14))
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(window, text ="4", command = lambda: add_to_calculation(4),width = 5, font = ("Arial",14))
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(window, text ="5", command = lambda: add_to_calculation(5),width = 5, font = ("Arial",14))
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(window, text ="6", command = lambda: add_to_calculation(6),width = 5, font = ("Arial",14))
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(window, text ="7", command = lambda: add_to_calculation(7),width = 5, font = ("Arial",14))
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(window, text ="8", command = lambda: add_to_calculation(8),width = 5, font = ("Arial",14))
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(window, text ="9", command = lambda: add_to_calculation(9),width = 5, font = ("Arial",14))
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(window, text ="0", command = lambda: add_to_calculation(0),width = 5, font = ("Arial",14))
btn_0.grid(row = 5, column = 2)
btn_plus = tk.Button(window, text ="+", command = lambda: add_to_calculation("+"),width = 5, font = ("Arial",14),bg ="gray")
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(window, text ="-", command = lambda: add_to_calculation("-"),width = 5, font = ("Arial",14),bg ="gray")
btn_minus.grid(row = 3, column = 4)
btn_mul = tk.Button(window, text ="*", command = lambda: add_to_calculation("*"),width = 5, font = ("Arial",14),bg="gray")
btn_mul.grid(row = 4, column = 4)
btn_dvi = tk.Button(window, text ="/", command = lambda: add_to_calculation("/"),width = 5, font = ("Arial",14),bg = "gray")
btn_dvi.grid(row = 5, column = 4)
btn_open = tk.Button(window, text ="(", command = lambda: add_to_calculation("("),width = 5, font = ("Arial",14))
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(window, text =")", command = lambda: add_to_calculation(")"),width = 5, font = ("Arial",14))
btn_close.grid(row = 5, column = 3)
btn_equals = tk.Button(window, text ="=", command = evaluate_calculation,width = 11, font = ("Arial",14),bg="light blue")
btn_equals.grid(row = 6, column = 3,columnspan=2)
btn_clear = tk.Button(window, text ="c", command = clear_field,width = 11, font = ("Arial",14),bg="light blue")
btn_clear.grid(row = 6, column = 1,columnspan=2)

window.mainloop()

print('__________________________________________________________________________________')

# (4)

window = tk.Tk()
window.title("loginApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(1,weight=2)
window.columnconfigure( 2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)


label1 =ttk.Label(window,text="User Name :",font="arial 20",background="light blue")
label1.grid(row=1,column=1,sticky="e")
entry_text=tk.StringVar()
entry1 = ttk.Entry(window,font="arial 12",width=15,textvariable=entry_text)
entry1.grid(row=1,column=2,sticky="w")
label2 =ttk.Label(window,text=" PassWord :",font="arial 20",background="light blue")
label2.grid(row=2,column=1,sticky="e")
entry_text1=tk.StringVar()
entry2 = ttk.Entry(window,font="arial 12",width=15,textvariable=entry_text1)
entry2.grid(row=2,column=2,sticky="w")
button =ttk.Button(window,text="Click For login",width=30)
button.place(relx=0.2,rely=0.5)

window.mainloop()
#___________________________________________________________________________________________________
#36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and
#ecrement buttonds.

import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("CounterApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
total_m= 1000000
label1 =ttk.Label(window,text="Your current account equal :",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
global_var =1000000
label2 =ttk.Label(window,text= global_var ,font="arial 12",background="green")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your amount...?')
def d_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var - new_m
    label2['text']= global_var

def i_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var + new_m
    label2['text']= global_var

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)
button1 =ttk.Button(window, text="Decrement button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")
button2 =ttk.Button(window, text="Increment button", width=22,command=i_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()



print('_____________________________________________________________________________')


# (5)


window = tk.Tk()
window.title("WeatherApp")
window.geometry("1100x600")
window.resizable(False,False)
window.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),weight=1)
window.rowconfigure((0,1,2,3),weight=1)



label = ttk.Label(window,text="WEATHER APP",font=("arial 40 bold"),background="#4a4a4a",foreground="white")
label.place(relx = 0.3,rely=0.1)
label1 = ttk.Label(window,text=" Province :",font=("arial 25"))
label1.grid(row=2,column=4)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=1)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=6)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=7)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=9)
entry_text=tk.StringVar(value="Searching...?   ")
entry = ttk.Entry(window,textvariable=entry_text,font='arial 20 ', background="#111111",foreground="black")
entry.grid(row=2,column =6)

button1 = ttk.Button(window,text= "    Today   : Kabul ---> Suuny * \n"
                                  
                                  "\n Tomorrow : Kabul ---> Rainy  ")
button1.grid(row=1,column =4 ,columnspan=3,sticky="nsew",padx =2,pady=2)
button2 = ttk.Button(window,text="    Today    : Bamyan ---> Sunny * \n"
                                  
                                  "\n Tomorrow : Bamyan ---> Rainy  ")
button2.grid(row=1,column =0 ,columnspan=4,sticky="nsew",padx =2,pady=2)
button3 = ttk.Button(window,text="    Today    : Herat ---> Cloudy \n"
                                  
                                  "\n Tomorrow : Herat ---> Sunny * ")
button3.grid(row=1,column =7,columnspan=4,sticky="nsew",padx =2,pady=2)
button4 = ttk.Button(window,text="       Today    : Helmand ---> Sunny * \n"
                                  
                                "\n      Tomorrow : Helmand ---> Rainy  ")
button4.grid(row=1,column =12 ,columnspan=4,sticky="nsew",padx =2,pady=2)
window.mainloop()

print('_____________________________________________________________________________________________')




