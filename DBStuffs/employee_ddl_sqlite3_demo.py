import sqlite3

# To create in-memory database
# conn = sqlite3.connect(':memory:')

# To create static file for using the sqlite db
conn = sqlite3.connect('employee.db')

# To execute the sql commands on this db, a cursor is needed.
cur = conn.cursor()

# To create db table
cur.execute("""
            CREATE TABLE EMPLOYEE(
                FIRST TEXT,
                LAST TEXT,
                PAY REAL
            )
            """)

conn.commit()

conn.close()


