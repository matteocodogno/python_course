from tkinter import *
from tkinter.font import names 

def convert():
    kilos = float(kg_value.get())
    grams = kilos * 1000
    pounds = kilos * 2.20462
    ounces = kilos * 35.274

    grams_txt.insert(END, grams)
    pounds_txt.insert(END, pounds)
    ounces_txt.insert(END, ounces)

window = Tk(baseName='Grams Pounds Ounces')

l1 = Label(window, text='Kg')
l1.grid(row=0, column=0)

kg_value = StringVar()
kg = Entry(window, textvariable=kg_value)
kg.grid(row=0, column=1)

convert_btn = Button(window, text='Execute', command=convert)
convert_btn.grid(row=0, column=2)


grams_txt = Text(window, height=1, width=20)
grams_txt.grid(row=1, column=0)

pounds_txt = Text(window, height=1, width=20)
pounds_txt.grid(row=1, column=1)

ounces_txt = Text(window, height=1, width=20)
ounces_txt.grid(row=1, column=2)

# needed to maintain program open
window.mainloop()
