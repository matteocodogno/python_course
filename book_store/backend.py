import contextlib
import sys
import sqlite3

def connectivity():
    cursor = None

    @contextlib.contextmanager
    def connect():
        nonlocal cursor 

        try:
            if cursor is None:
                connection = sqlite3.connect('books.db')
                with connection:
                    cursor = connection.cursor()
                    yield cursor
            else:
                yield cursor
        finally:
            cursor.close()
            cursor = None

    return connect


def init_schema():
    with cursor_factory() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')


def insert(title, author, year, isbn):
    with cursor_factory() as cursor:
        cursor.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))


def list_all():
    with cursor_factory() as cursor:
        cursor.execute('SELECT * FROM books')
        return cursor.fetchall()


def search(title='', author='', year='', isbn=''):
    with cursor_factory() as cursor:
        cursor.execute('SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
        return cursor.fetchall()


def delete(id):
    with cursor_factory() as cursor:
        cursor.execute('DELETE FROM books WHERE id=?', (id,))


def update(id, title, author, year, isbn):
    with cursor_factory() as cursor:
        cursor.execute('UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))


def init():
    try:
        init_schema()
    except Exception as err:
        print('unexpected error ', err)
        sys.exit(1)


cursor_factory = connectivity()
init()
