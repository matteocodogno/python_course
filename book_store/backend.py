import contextlib
import sys
import sqlite3

class BookRepository:

    def __init__(self, db) -> None:
        self.connection_factory = self.connectivity(db)
        try: 
            self.init_schema()
        except Exception as err:
            print('unexpected error ', err)
            sys.exit(1)


    def connectivity(self, db):
        connection = None

        @contextlib.contextmanager
        def connect():
            nonlocal connection

            if connection is None:
                connection = sqlite3.connect(db)
                with connection:
                    yield connection
            else:
                yield connection

        return connect


    def init_schema(self):
        with self.connection_factory() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')


    def insert(self, title, author, year, isbn):
        with self.connection_factory() as cursor:
            cursor.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))


    def list_all(self):
        with self.connection_factory() as cursor:
            return cursor.execute('SELECT * FROM books')


    def search(self, title='', author='', year='', isbn=''):
        with self.connection_factory() as cursor:
            return cursor.execute('SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))


    def delete(self, id):
        with self.connection_factory() as cursor:
            cursor.execute('DELETE FROM books WHERE id=?', (id,))


    def update(self, id, title, author, year, isbn):
        with self.connection_factory() as cursor:
            cursor.execute('UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
 

    def __del__(self):
        with self.connection_factory() as conn:
            conn.close()
