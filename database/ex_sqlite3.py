import sqlite3


def create_table():
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
        cur.commit()


def insert(item, quantity, price):
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO store VALUES (?, ?, ?)', (item, quantity, price))


def view():
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor();
        cur.execute('SELECT * FROM store')
        return cur.fetchall()


def delete(item):
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM store WHERE item=?', (item,))


def update(item, quantity, price):
    with sqlite3.connect('lite.db') as conn:
        cur = conn.cursor()
        cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (quantity, price, item))


# insert('Wine Glass', 10, 5)
# insert('Water Glass', 7, 2)
# insert('Coffee cup', 3, 2)


# delete('Wine Glass')
update('Water Glass', 4, 1)
print(view())
