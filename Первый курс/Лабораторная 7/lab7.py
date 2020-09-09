#-*- coding: utf-8 -*-#
#Импорт модулей
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter.simpledialog as tsimp

#Функция отвечающая за открытие файла с записью полученного текста в глобальную переменную
def insertText():
    global read
    file_name = fd.askopenfilename()
    f = open(file_name, encoding="utf-8")
    read = f.read()
    text.insert(1.0, read)
    f.close()

#Функция отвечающая за сохранение обработанного текста в новый файл
def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

#Функция преобразования текста, а также дополнительное окно для ввода данных пользователя
def transformation():
    result = tsimp.askstring(title='Номер зачетной книжки', prompt='Введите номер зачетки')
    coms = (f'<!DOCTYPE html>\n<html lang="en" dir="ltr">\n  <head>\n    <meta charset="utf-8">\n    <title>{result}</title>\n  </head>\n  <body>\n    <center><h1>{read}'f'</h1></center>\n  </body>\n</html>')
    text.delete(1.0, END)
    text.insert(1.0, coms)
    mb.showinfo('Успешно!', 'Преобразование выполнено')
    
#Основной код программы отвечающий за создание элементов интерфейса
root = Tk()
root.title("Преобразователь")
text = Text(width=100, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)
b3 = Button(text="Преобразовать", command=transformation)
b3.grid(row=1, column=1, sticky=E)

root.mainloop()
