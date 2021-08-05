import sqlite3

from employee import Employee

conn = sqlite3.connect('./Day_XX/Sqlite/employee.db')
cur = conn.cursor()
# cur.execute(""" CREATE TABLE employees(
#             first text,
#             last text,
#             pay integer
#             )""")

emp_1 = Employee("Master","Bara", 100000)
emp_2 = Employee("Anna","Bara", 15)
# emp_2 = Employee("Victor","Virgin", 0)

# cur.execute("INSERT INTO employees VALUES(?,?,?), (emp_1.first, emp_1.last, emp_1.pay)")
# cur.execute("INSERT INTO employees VALUES(:first,:last,:pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay} )
# cur.execute("INSERT INTO employees VALUES('Aang', 'Bara', '10000' ) ")
# emp_1 = Employee('John', 'Doe', 80000)
# emp_2 = Employee('Jane', 'Doe', 90000)

# cur.execute("INSERT INTO employees VALUES(:first,:last,:pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})
# cur.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

cur.execute("SELECT * FROM employees WHERE last = 'Bara'")
print(cur.fetchall())
cur.execute("SELECT * FROM employees WHERE last =:last", {'last':'Doe'})
print(cur.fetchall())
conn.commit()
conn.close()
