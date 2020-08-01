class Employee(object):
    def __init__(self, fullname, **kwargs):
        names = fullname.split(' ')
        self.name = names[0]
        self.lastname = names[1]
        self.__dict__.update(kwargs)


def main():
    john = Employee('John Doe')
    mary = Employee('Mary Major', salary=120000)
    richard = Employee('Richard Roe', salary=110000, height=178)
    giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
    peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese',
                    subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])

    assert (john.lastname == 'Doe')

    if __name__ == '__main__':
        main()
