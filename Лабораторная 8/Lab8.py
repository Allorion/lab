#-*- coding: utf-8 -*-#
#Импорт модулей
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter.simpledialog as tsimp
import Lab8_huff as huff

#Функция отвечающая за открытие файла с записью полученного текста в глобальную переменную
#Открытие файла с текстом
def insertText():
    global read
    file_name = fd.askopenfilename()
    f = open(file_name, encoding="utf-8")
    read = f.read()
    text.insert(1.0, read)
    f.close()
#Открытие файла с ключом
def insertText_key():
    global key2
    file_name = fd.askopenfilename()
    f = open(file_name, encoding="utf-8")
    key2 = f.read()
    key2 = eval(key2)
    f.close()

#Функция отвечающая за сохранение обработанного текста в новый файл
def extractText_encry():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
#Сохранение зашифрованного файла
    f = open(file_name, 'w', encoding="utf-8")
    s = text.get(1.0, END)
    f.writelines(s)
    f.close()
#Сохранение ключа с расширением .dat
    f = open(f'{file_name}.key.dat', 'w', encoding="utf-8")
    f.write(key)
    f.close()

#Функция отвечающая за сохранение расшифрованного файла
def extractText_decip():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w', encoding="utf-8")
    f.writelines(decod)
    f.close()
#Функция шифрования
def encryption():
    global key
    content = huff.encryption_text(read)
    key = huff.encryption_key(read)
    key = str(key)
    text.delete(1.0, END)
    text.insert(1.0, content)
    mb.showinfo('Успешно!', 'Шифрование выполнено')

#Функция расшифровки
def decipherment():
    global decod
    decod = huff.huff_decompress(read, key2)
    decod = str(decod)
    text.delete(1.0, END)
    text.insert(1.0, decod)
    mb.showinfo('Успешно!', 'Шифрование выполнено')

#Основной код программы отвечающий за создание элементов интерфейса
root = Tk()

#Функция отвечающая за переключение между зашифровкой и расшифровкой
def passw():
    global b1, b2, b3, b4, b5, b6, b7

    if selected.get() == 1:
        b1 = Button(text="Открыть текст", command=insertText)
        b1.grid(row=1, sticky=E)
        b2 = Button(text="Сохранить", command=extractText_encry)
        b2.grid(row=1, column=2)
        b3 = Button(text="Конвертация", command=encryption)
        b3.grid(row=1, column=1, sticky=E)
        b4.grid_remove()
        b5.grid_remove()
        b6.grid_remove()
        b7.grid_remove()

    if selected.get() == 2:
        b4 = Button(text="Конвертация", command=decipherment)
        b4.grid(row=1, column=1, sticky=E)
        b5 = Button(text="Открыть шифр", command=insertText)
        b5.grid(row=1, sticky=E)
        b6 = Button(text="Открыть ключ", command=insertText_key)
        b6.grid(row=1, column=1, sticky=W)
        b7 = Button(text="Сохранить", command=extractText_decip)
        b7.grid(row=1, column=2)
        b1.grid_remove()
        b2.grid_remove()
        b3.grid_remove()


selected = IntVar()
rad1 = Radiobutton(root,text='Шифрование', value=1, variable=selected, command=passw)
rad2 = Radiobutton(root,text='Дешифровка', value=2, variable=selected, command=passw)
lbl = Label(root)
rad1.grid(row=1, column=0)
rad2.grid(row=2, column=0)

root.title("Преобразователь")
text = Text(width=100, height=25)
text.grid(columnspan=2)



root.mainloop()
