import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
dbname = os.getenv('db')
user = os.getenv('user')
password = os.getenv('pass')
host = os.getenv('host')
port = os.getenv('port')


def create_table():
    with psycopg2.connect(f'dbname=\'{dbname}\' user=\'{user}\' password=\'{password}\' host=\'{host}\' port=\'{port}\'') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')


def insert(item, quantity, price):
    with psycopg2.connect(f'dbname=\'{dbname}\' user=\'{user}\' password=\'{password}\' host=\'{host}\' port=\'{port}\'') as conn:
        cur = conn.cursor()
        # cur.execute(f'INSERT INTO store VALUES (\'{item}\', \'{quantity}\', \'{price}\')')
        cur.execute('INSERT INTO store VALUES (%s,%s,%s)', (item, quantity, price))


def view():
    with psycopg2.connect(f'dbname=\'{dbname}\' user=\'{user}\' password=\'{password}\' host=\'{host}\' port=\'{port}\'') as conn:
        cur = conn.cursor();
        cur.execute('SELECT * FROM store')
        return cur.fetchall()


def delete(item):
    with psycopg2.connect(f'dbname=\'{dbname}\' user=\'{user}\' password=\'{password}\' host=\'{host}\' port=\'{port}\'') as conn:
        cur = conn.cursor()
        cur.execute('DELETE FROM store WHERE item=%s', (item,))


def update(item, quantity, price):
    with psycopg2.connect(f'dbname=\'{dbname}\' user=\'{user}\' password=\'{password}\' host=\'{host}\' port=\'{port}\'') as conn:
        cur = conn.cursor()
        cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (quantity, price, item))


create_table()

# insert('Apple', 3, 2)
# insert('Orange', 1, 2.5)
# insert('Wine Glass', 10, 5)
# insert('Water Glass', 7, 2)
# insert('Coffee cup', 3, 2)

# delete('Orange')
update('Water Glass', 4, 1)
print(view())
