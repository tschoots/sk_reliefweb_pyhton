

class Employee:
    'common base class for all employees'
    empCount = 0
    ''' 
    comment 
    '''

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Created : %s" % self.name)
        Employee.empCount += 1


    def __del__(self):
        print("Deleted : %s" % self.name)
        Employee.empCount -= 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)


    def displayEmployee(self):
        print("Name : %s, Salary : %d" % (self.name , self.salary))

    def formatedEmpString(self, nroftimes):
        return "formated Name : %s, Salary %d" % (self.name, self.salary)


class Driver(Employee):

    def whoami(self):
        print("driver")


if __name__ == "__main__":
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

