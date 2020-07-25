class Employee:

    def __init__(self, firstname='', lastname='', salary=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_string(cls, dashed_string):
        emp = Employee()
        ls = dashed_string.split("-")
        emp.firstname = ls[0]
        emp.lastname = ls[1]
        emp.salary = int(ls[2])
        return emp


def main():
    # Initialize objects
    emp1 = Employee("Mary", "Sue", 60000)
    emp2 = Employee.from_string("John-Smith-55000")
    emp3 = Employee.from_string("Susan-Walker-70000")
    emp4 = Employee.from_string("Michael-Ferry-90000")
    emp5 = Employee("Graham", "Derrell", 55000)

    # Evaluate Test Cases
    assert (emp1.firstname == "Mary")
    assert (emp1.lastname == "Sue")
    assert (emp1.salary == 60000)
    assert (emp2.firstname == "John")
    assert (emp2.lastname == "Smith")
    assert (emp2.salary == 55000)
    assert (emp3.firstname == "Susan")
    assert (emp3.lastname == "Walker")
    assert (emp3.salary == 70000)
    assert (emp4.firstname == "Michael")
    assert (emp4.lastname == "Ferry")
    assert (emp4.salary == 90000)
    assert (emp5.firstname == "Graham")
    assert (emp5.lastname == "Derrell")
    assert (emp5.salary == 55000)

    print('All test cases validated.')


if __name__ == '__main__':
    main()
