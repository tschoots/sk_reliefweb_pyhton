from Employee import Employee, Driver


# this would create first object of Employee class
emp1 = Employee("Zara", 2000)
# this would create second object of Employee class
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)
del emp2
str_emp1 = emp1.formatedEmpString(5)
print(str_emp1)
print("Total Employee %d" % Employee.empCount)
print(Employee.__doc__)

for i in range(5):
    print("nr : %d" % i)

driver = Driver("John", 4000)
driver.formatedEmpString(5)
driver.whoami()