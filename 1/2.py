# импортируем библиотеку tkinter в код
from tkinter import *

# создаём наше окно root
root = Tk()

# массивчик
a = ["chto", "kak", "eto", "delat", "chto",
     "kak", "eto", "delat", "chto", "kak",
     "eto", "delat", "chto", "kak", "eto",
     "delat", "chto", "kak", "eto", "delat",
     "chto", "kak", "eto", "delat", "chto",
     "kak", "eto", "delat", "chto", "kak"]

# хочу вывести каждый i-й элемент в новой строке нашего окна
for i in range(30):
    # создаём надпись, выводящую массив целиком
    the_label = Label(root, text=(a[i]), bg="blue", fg="yellow")
    #                           бэкграунд 👆 синий, а надпись жёлтая
    # пакуем надпись
    the_label.pack(fill=X)
#          а вот ТУТ 👆 я растягиваю надпись по ширине окна,
#                         иначе некрасиво выглядит

# также нужно зациклить наше окно, иначе
# оно [не появится / мгновенно пропадёт]
root.mainloop()