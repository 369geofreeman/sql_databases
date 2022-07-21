import sqlite3


# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Create a table
# ---
# c.execute('''
#     CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )''')


# Insert single value at a time into a table
# ---
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Time', 'Smith', 'tim@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")
# print("Command executed successfully...")


# Insert many values at once into a table
# ---
# many_customers = [('Wes', 'Brown', "wes@brown.com"),
#                   ('Steph', 'Kuewa', "steph@kuewa.com"),
#                   ('Dan', 'Pas', "dan@pas.com"),
#                   ]

# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
# print(
#     f"Command executed successfully, {len(many_customers)} values added to table...")


# Query a database
# ---
# c.execute("SELECT * FROM customers")
# c.fetchone()    # gets the first entry [tuple]
# c.fetchmany(3)  # Gets an amount [list]
# c.fetchall()    # Gets all [list]

# items = c.fetchall()

# print("Members in customes")
# for idx, customer in enumerate(items):
#     print(
#         f"\nMember {idx+1}\n---\nName: \t{customer[0]} {customer[1]}\nEmail: \t{customer[2]}")


# Getting the primary key
# ---
# c.execute("SELECT rowid, * FROM customers")

# items = c.fetchall()

# for item in items:
#     print(item)


# Searching or getting specific things from database
# ---

# Exact match
# c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")

# A match where you don't specify all of the info (brings back all results that starts with, ends with etc)
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# c.execute("SELECT * FROM customers WHERE email LIKE '%codemy.com'")

# items = c.fetchall()

# for item in items:
#     print(item)

# With numbers we can also use logical opperators
# c.execute("SELECT * FROM customers WHERE age > 21")


# update records
# ---

# Use the rowid instead of anything else to change things
# c.execute("""
#         UPDATE customers SET first_name = 'Marty' WHERE rowid = 3
#         """)
# conn.commit()

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
#     print(item)


# Delete a record
# ---
# c.execute("DELETE FROM customers WHERE rowid = 6")
# conn.commit()

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
#     print(item)


# Ordering results by
# ---
# ASC = ascending
# DESC = decending
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# items = c.fetchall()
# for i in items:
#     print(i)


# AND / OR (extend the functionallity of the where clause)
# ---
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND rowid = 3")

# items = c.fetchall()
# for i in items:
#     print(i)

# Limit results
# ---
# c.execute("SELECT rowid, * FROM customers LIMIT 2")

# items = c.fetchall()
# for i in items:
#     print(i)

# Drop / delete a table
# c.execute("DROP TABLE customers")
# conn.commit()
# items = c.fetchall()
# for i in items:
#     print(i)


# Commit to database
conn.commit()

# Close our connection
conn.close()
