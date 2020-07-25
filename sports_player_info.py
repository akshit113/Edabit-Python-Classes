class player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        str_age = str(self.age)
        res_str = '{} is age {}'.format(self.name, str_age)
        return res_str

    def get_height(self):
        str_height = str(self.height)
        res_str = '{} is {}cm'.format(self.name, str_height)
        return res_str

    def get_weight(self):
        str_weight = str(self.weight)
        res_str = '{} weighs {}kg'.format(self.name, str_weight)
        return res_str


def main():
    player1 = player('Patrick Mahomes', 24, 188, 104)
    player2 = player('Jimmy Garoppolo', 28, 188, 102)
    player3 = player('Julio Jones', 31, 191, 100)

    assert (player1.get_age(), 'Patrick Mahomes is age 24')
    assert (player1.get_height(), 'Patrick Mahomes is 188cm')
    assert (player1.get_weight(), 'Patrick Mahomes weighs 104kg')
    assert (player2.get_age(), 'Jimmy Garoppolo is age 28')
    assert (player2.get_height(), 'Jimmy Garoppolo is 188cm')
    assert (player2.get_weight(), 'Jimmy Garoppolo weighs 102kg')
    assert (player3.get_age(), 'Julio Jones is age 31')
    assert (player3.get_height(), 'Julio Jones is 191cm')
    assert (player3.get_weight(), 'Julio Jones weighs 100kg')


if __name__ == '__main__':
    main()
