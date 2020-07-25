# Edabit: https://edabit.com/challenge/7FyTyi68Df2CxLx6C

class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number

    @classmethod
    def garden_feast(cls):
        Pizza.ingredients = ['spinach', 'olives', 'mushroom']
        return cls(Pizza.ingredients)

    @classmethod
    def meat_festival(cls):
        Pizza.ingredients = ['beef', 'meatball', 'bacon']
        return cls(Pizza.ingredients)

    @classmethod
    def hawaiian(cls):
        # Pizza.order_number += 1
        Pizza.ingredients = ['ham', 'pineapple']
        return cls(Pizza.ingredients)


def main():
    p1 = Pizza(["bacon", "parmesan", "ham"])
    p2 = Pizza.garden_feast()
    p3 = Pizza.hawaiian()
    p4 = Pizza.meat_festival()
    p5 = Pizza(["pepperoni", "bacon"])
    my_pizza = Pizza(["cheese", "caviar", "oyster", "uranium"])

    print(p1.ingredients == ["bacon", "parmesan", "ham"])
    print(p2.ingredients == ["spinach", "olives", "mushroom"])
    print(p3.ingredients == ["ham", "pineapple"])
    print(p4.ingredients == ["beef", "meatball", "bacon"])
    print(p5.ingredients == ["pepperoni", "bacon"])
    print(my_pizza.ingredients == ["cheese", "caviar", "oyster", "uranium"])
    print(p1.order_number == 1)
    print(p2.order_number == 2)
    print(p3.order_number == 3)
    print(p4.order_number == 4)
    print(p5.order_number == 5)
    print(my_pizza.order_number == 6)

    print('done')


if __name__ == '__main__':
    main()
