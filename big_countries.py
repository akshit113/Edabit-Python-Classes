class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.population_density = self.population / self.area
        self.is_big = False
        if (population > 250000000) | (area > 3000000):
            self.is_big = True

    def compare_pd(self, other):
        res_str = ''
        if self.population_density > other.population_density:
            res_str = '{} has a larger population density than {}'.format(self.name, other.name)
        if self.population_density < other.population_density:
            res_str = '{} has a smaller population density than {}'.format(self.name, other.name)
        return res_str


def main():
    australia = Country('Australia', 23545500, 7692024)
    andorra = Country('Andorra', 76098, 468)
    brazil = Country('Brazil', 202794000, 8515767)
    china = Country('China', 1393000000, 9597000)
    madagascar = Country('Madagascar', 26260000, 587000)

    assert australia.is_big
    assert (australia.compare_pd(andorra) == 'Australia has a smaller population density than Andorra')

    assert andorra.is_big
    assert (andorra.compare_pd(australia) == 'Andorra has a larger population density than Australia')

    assert brazil.is_big
    assert (brazil.compare_pd(china) == 'Brazil has a smaller population density than China')

    assert china.is_big
    assert (china.compare_pd(madagascar) == 'China has a larger population density than Madagascar')

    assert madagascar.is_big
    assert (madagascar.compare_pd(australia) == 'Madagascar has a larger population density than Australia')

    print('all tests validated')


if __name__ == '__main__':
    main()
