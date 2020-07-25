class Composer:
    count = 0

    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count += 1


def main():
    assert (Composer.count == 0)

    c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
    assert (Composer.count == 1)

    c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
    c3 = Composer("Johannes Brahms", 1833, "Germany")
    Test.assert_equals(Composer.count, 3)

    c4 = Composer("Richard Wagner", 1813, "Germany")
    c5 = Composer("Claude Debussy", 1862, "France")
    c6 = Composer("Richard Tchaikovsky", 1840, "Russia")
    c7 = Composer("Frederic Chopin", 1810, "Poland")
    Test.assert_equals(Composer.count, 7)

    c8 = Composer("Joseph Haydn", 1732, "Austria")
    Test.assert_equals(Composer.count, 8)


if __name__ == '__main__':
    main()
