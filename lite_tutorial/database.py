import sqlite3


# Connect to database
conn = sqlite3.connect("customer.db")

# Create a cursor
c = conn.cursor()

# Create a table
# c.execute('''
#     CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )''')

# Insert single value at a time into a table
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Time', 'Smith', 'tim@codemy.com')")
# c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@codemy.com')")
# print("Command executed successfully...")

many_customers = [('Wes', 'Brown', "wes@brown.com"),
                  ('Steph', 'Kuewa', "steph@kuewa.com"),
                  ('Dan', 'Pas', "dan@pas.com"),
                  ]

# Insert many values at once into a table
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
print(
    f"Command executed successfully, {len(many_customers)} values added to table...")

# Commit to database
conn.commit()

# Close our connection
conn.close()
