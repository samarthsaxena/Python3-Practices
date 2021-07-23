import sqlite3

from DBStuffs.employee import Employee

conn = sqlite3.connect("employee.db")

cur = conn.cursor()

emp1 = Employee('jibba', 'jabba', 200000)
emp2 = Employee('nibba', 'nubba', 3201020)

# A very common and NON-Standard way of constructing the query,
# Using string formatting
cur.execute(f'INSERT INTO EMPLOYEE values ({emp1.first},{emp1.last},{emp1.pay})')
conn.commit()
# There are 2 Standard ways too
# 1. Using the place holder param
cur.execute("INSERT into EMPLOYEE values (?,?,?)", (emp2.first, emp2.last, emp2.pay))
conn.commit()
# 2. Using named place holder (which work as a key ) and passing the values from objects
# This way is more readable
cur.execute("INSERT into EMPLOYEE values (:first, :last, :pay)",
            {'first': emp1.first, 'last': emp1.last, 'pay': emp1.pay})
conn.commit()


all_data = cur.fetchall()
print(f'Total entries {len(all_data)}')
for employee_data in all_data:
    print(employee_data)


conn.close()