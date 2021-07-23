import sqlite3

# To create in-memory database
# conn = sqlite3.connect(':memory:')

# To create static file for using the sqlite db
conn = sqlite3.connect('employee.db')

# To execute the sql commands on this db, a cursor is needed.
cur = conn.cursor()


# Insert query
cur.execute("INSERT INTO EMPLOYEE VALUES('Test1','Employee1',20000001.122)")

conn.commit()

# Select query
cur.execute("Select * from Employee")
#print(cur.fetchmany(2))
print(cur.fetchall())
# print(cur.fetchone())

conn.close()


