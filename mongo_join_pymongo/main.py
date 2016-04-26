__author__ = 'premaseem'

from pymongo import Connection
c = Connection()
db = c.test

db.employee.drop()
db.employeeSalary.drop()

db.test.insert({"name":"premaseem"})
obj1 = {"eid":1,"name":"premaseem"}
obj2 = {"eid":2,"name":"sony"}
obj3 = {"eid":3,"name":"meera"}
bulk_employee_insert = [obj1,obj2,obj3]

# insert salary
db.employee.insert(bulk_employee_insert)

objs1 = {"eid":1,"salary":1000}
objs2 = {"eid":2,"salary":8000}
objs3 = {"eid":3,"salary":25}
bulk_salary_insert = [objs1,objs2,objs3]

db.employeeSalary.insert(bulk_salary_insert)

print str(db.employee.count()) + str("total employee")
print str(db.employeeSalary.count()) + str("total salary")

def find_employee():
    emp_obj = db.employee.find_one({"eid":1})
    print emp_obj

def find_employee_with_joined_salary(eid) :
    emp_obj = db.employee.find_one({"eid":eid})
    emp_sal_obj = db.employeeSalary.find_one({"eid":eid})
    emp_obj["salary"] = emp_sal_obj["salary"]
    del emp_obj["_id"]
    print emp_obj

find_employee_with_joined_salary(2)
