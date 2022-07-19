import sqlite3
import os


conn = sqlite3.connect('organization_count.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')

if (len(fname) < 1):
    fname = 'm-box.txt'

fh = open(os.path.join(os.path.dirname(__file__), fname))

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    org = pieces[1].split('@')[-1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))

    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))

conn.commit()


# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
count = 0

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    count += int(row[1])

print(count)

cur.close()
