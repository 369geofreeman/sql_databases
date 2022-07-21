import database


# Add a record to the database
# database.add_one("Lora", "Smith", "lora@smith.com")

# Adds many records to the database
# many_customers = [('Wes', 'Brown', "wes@brown.com"),
#                   ('Steph', 'Kuewa', "steph@kuewa.com"),
#                   ('Dan', 'Pas', "dan@pas.com"),
#                   ]
# database.add_many(many_customers)


# query user email
database.email_lookup("steph@kuewa.com")

# Delete a record from the database (use rowid as string)
# database.delete_one('5')

# Show all records
database.show_all()
