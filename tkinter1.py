from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid(column=0, row=1)

c = Canvas(root, width=200, height=200, bg='white')
c.grid(column=0, row=0)
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
ttk.Entry(frm).grid(column=0, row=1)

mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")
mainmenu.add_cascade(label="Файл",
                     menu=filemenu)


c.create_line(10, 10, 190, 50)

c.create_line(100, 180, 100, 60, fill='green',
              width=5, arrow=LAST, dash=(10, 2),
              activefill='lightgreen',
              arrowshape="10 20 10")

root.mainloop()