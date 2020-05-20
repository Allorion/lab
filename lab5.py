from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

#Создание окна программы
root = Tk()
root.title("Калькулятор v1.0")#Название окна

#Логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Первый символ не число")
            messagebox.showerror("Ошибка, вы не ввели номер")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибка")
            messagebox.showerror("Ошибка! Проверьте данные")

#Очистить поле
    elif key == "C":
        calc_entry.delete(0, END)
#Знак +-
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        sin=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.sin(float(sin)))
    elif key == "cos":
        cos=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.cos(float(cos)))
    elif key == "tan":
        tan=calc_entry.get()
        calc_entry.delete(0)
        calc_entry.insert(END, math.tan(float(tan)))
    elif key == "(":
            calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)


#Кнопки
bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"tan","(", ")"


]
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1
calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
