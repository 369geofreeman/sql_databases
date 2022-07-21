import sqlite3


def show_all():
    '''Query database and return all records'''

    # Connect to the database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    # query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit our command
    conn.commit()
    # Close our connection
    conn.close()


def add_one(first, last, email):
    '''add a new record to the table'''

    conn = sqlite3.connect('customer.db')

    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))

    conn.commit()
    conn.close()


def add_many(lst):
    '''adds many records to the table'''

    conn = sqlite3.connect('customer.db')

    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (lst))

    conn.commit()
    conn.close()


def email_lookup(email):
    '''Looks up email from table'''
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()


def delete_one(id):
    '''Removes one record from table'''
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", (id))

    conn.commit()
    conn.close()
