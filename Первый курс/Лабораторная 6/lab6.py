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


#Индивидуальное задание
#Функция отвечающая за логику программы и расчетов
def clicked():
    if chk_state.get() == 1:
        if selected.get() == 1:
            cdh=calc_entry.get()
            dhanush = float(cdh)/183
            calc_entry.insert(END, (f'см = {dhanush}Дхануш'))
        else:
            calc_entry.insert(END, "Ошибка, не верная система мер ")
    elif chk_state2.get() == 1:
        if selected.get() == 2:
            dm = calc_entry.get()
            dam = float(dm)/20.9628
            calc_entry.insert(END, (f'гр = {dam}Дам'))
        else:
            calc_entry.insert(END, "Ошибка, не верная система мер ")
    elif chk_state3.get() == 1:
        if selected.get() == 3:
            adh = calc_entry.get()
            adhaka = float(adh)/3.9
            calc_entry.insert(END, (f'л = {adhaka}Адхака'))
        else:
            calc_entry.insert(END, "Ошибка, не верная система мер ")


#Добавляем кнопку перевода
btn = Button(root, text="Перевод", command=clicked)
btn.grid(column=4, row=0, sticky="nsew")
#Просто надпись
lbl1 = Label(root, text="Исходная единица")
lbl1.grid(column=6, row=0)
#Просто надпись
lbl2 = Label(root, text="Требуемая")
lbl2.grid(column=6, row=2)
#Добавляем радиокнопки (Переключатель)
selected = IntVar()
rad1 = Radiobutton(root,text='Сантиметры', value=1, variable=selected)
rad2 = Radiobutton(root,text='Граммы', value=2, variable=selected, command=clicked)
rad3 = Radiobutton(root,text='Литры', value=3, variable=selected, command=clicked)
lbl = Label(root)
rad1.grid(column=5, row=1)
rad2.grid(column=6, row=1)
rad3.grid(column=7, row=1)
#Добавляем флажок
chk_state = BooleanVar()
chk_state.set(False)
chk = Checkbutton(root, text='Дхануш', var=chk_state)
chk.grid(column=5, row=3)

chk_state2 = BooleanVar()
chk_state2.set(False)
chk = Checkbutton(root, text='Дам', var=chk_state2)
chk.grid(column=6, row=3)

chk_state3 = BooleanVar()
chk_state3.set(False)
chk = Checkbutton(root, text='Адхака', var=chk_state3)
chk.grid(column=7, row=3)


root.mainloop()
