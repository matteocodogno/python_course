import backend as be
from tkinter import *

window = Tk()

# Labels
title = Label(window, text='Title')
title.grid(row=0, column=0)
author = Label(window, text='Author')
author.grid(row=0, column=2)
year = Label(window, text='Year')
year.grid(row=1, column=0)
isbn = Label(window, text='ISBN')
isbn.grid(row=1, column=2)

# Input Text
title_value = StringVar()
title_input = Entry(window, textvariable=title_value)
title_input.grid(row=0, column=1)

author_value = StringVar()
author_input = Entry(window, textvariable=author_value)
author_input.grid(row=0, column=3)

year_value = StringVar()
year_input = Entry(window, textvariable=year_value)
year_input.grid(row=1, column=1)

isbn_value = StringVar()
isbn_input = Entry(window, textvariable=isbn_value)
isbn_input.grid(row=1, column=3)

# List
result_list = Listbox(window)
result_list.grid(row=2, column=0, columnspan=2, rowspan=6)
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

result_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=result_list.yview)


def onselect(evt):
    w = evt.widget
    tindex = w.curselection()
    if tindex is not None and len(tindex) > 0:
        index = tindex[0]
        _, title, author, year, isbn = w.get(index)
        title_value.set(title)
        author_value.set(author)
        year_value.set(year)
        isbn_value.set(isbn)


result_list.bind('<<ListboxSelect>>', onselect)


def clear_form():
    title_value.set('')
    author_value.set('')
    year_value.set('')
    isbn_value.set('')
    result_list.select_clear(0, END)


def view_command():
    result_list.delete(0, END)
    for row in be.list_all():
        result_list.insert(END, row)


def add_command():
    be.insert(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()
    clear_form()


def search_command():
    result_list.delete(0, END)
    for row in be.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        result_list.insert(END, row)


def delete_command():
    id, *_ = result_list.get(ACTIVE)
    be.delete(id)
    view_command()


def update_command():
    id, *_ = result_list.get(ACTIVE)
    be.update(id, title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    view_command()
    clear_form()


def close_command():
    window.destroy()


# Buttons
all_btn = Button(window, text='View all', command=view_command, width=12)
all_btn.grid(row=2, column=3)

search_btn = Button(window, text='Search entry', command=search_command, width=12)
search_btn.grid(row=3, column=3)

add_btn = Button(window, text='Add entry', command=add_command, width=12)
add_btn.grid(row=4, column=3)

update_btn = Button(window, text='Update', command=update_command, width=12)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text='Delete', command=delete_command, width=12)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text='Close', command=close_command, width=12)
close_btn.grid(row=7, column=3)

view_command()
window.mainloop()
