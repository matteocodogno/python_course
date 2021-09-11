from backend import BookRepository
from tkinter import *

class Gui:

    def __init__(self):
        self.bookRepository = BookRepository('books.db')
        self.window = Tk()
        self.render()

    def render(self):
        # Labels
        title = Label(self.window, text='Title')
        title.grid(row=0, column=0)
        author = Label(self.window, text='Author')
        author.grid(row=0, column=2)
        year = Label(self.window, text='Year')
        year.grid(row=1, column=0)
        isbn = Label(self.window, text='ISBN')
        isbn.grid(row=1, column=2)

        # Input Text
        self.title_value = StringVar()
        title_input = Entry(self.window, textvariable=self.title_value)
        title_input.grid(row=0, column=1)

        self.author_value = StringVar()
        author_input = Entry(self.window, textvariable=self.author_value)
        author_input.grid(row=0, column=3)

        self.year_value = StringVar()
        year_input = Entry(self.window, textvariable=self.year_value)
        year_input.grid(row=1, column=1)

        self.isbn_value = StringVar()
        isbn_input = Entry(self.window, textvariable=self.isbn_value)
        isbn_input.grid(row=1, column=3)

        # List
        self.result_list = Listbox(self.window)
        self.result_list.grid(row=2, column=0, columnspan=2, rowspan=6)
        scrollbar = Scrollbar(self.window)
        scrollbar.grid(row=2, column=2, rowspan=6)

        self.result_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.result_list.yview)

        self.result_list.bind('<<ListboxSelect>>', self.onselect)
 
        # Buttons
        all_btn = Button(self.window, text='View all', command=self.view_command, width=12)
        all_btn.grid(row=2, column=3)

        search_btn = Button(self.window, text='Search entry', command=self.search_command, width=12)
        search_btn.grid(row=3, column=3)

        add_btn = Button(self.window, text='Add entry', command=self.add_command, width=12)
        add_btn.grid(row=4, column=3)

        update_btn = Button(self.window, text='Update', command=self.update_command, width=12)
        update_btn.grid(row=5, column=3)

        delete_btn = Button(self.window, text='Delete', command=self.delete_command, width=12)
        delete_btn.grid(row=6, column=3)

        close_btn = Button(self.window, text='Close', command=self.close_command, width=12)
        close_btn.grid(row=7, column=3)

        self.view_command()
        self.window.mainloop()

 
    def onselect(self, evt):
        w = evt.widget
        tindex = w.curselection()
        if tindex is not None and len(tindex) > 0:
            index = tindex[0]
            _, title, author, year, isbn = w.get(index)
            self.title_value.set(title)
            self.author_value.set(author)
            self.year_value.set(year)
            self.isbn_value.set(isbn)


    def clear_form(self):
        self.title_value.set('')
        self.author_value.set('')
        self.year_value.set('')
        self.isbn_value.set('')
        self.result_list.select_clear(0, END)


    def view_command(self):
        self.result_list.delete(0, END)
        for row in self.bookRepository.list_all():
            self.result_list.insert(END, row)


    def add_command(self):
        self.bookrepository.insert(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.view_command()
        self.clear_form()


    def search_command(self):
        self.result_list.delete(0, END)
        for row in self.bookRepository.search(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()):
            self.result_list.insert(END, row)


    def delete_command(self):
        id, *_ = self.result_list.get(ACTIVE)
        self.bookRepository.delete(id)
        self.view_command()


    def update_command(self):
        id, *_ = self.result_list.get(ACTIVE)
        self.bookRepository.update(id, self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.view_command()
        self.clear_form()


    def close_command(self):
        self.window.destroy()

gui = Gui()