prices = {
    "Strawberries": "$1.50",
    "Banana": "$0.50",
    "Mango": "$2.50",
    "Blueberries": "$1.00",
    "Raspberries": "$1.00",
    "Apple": "$1.75",
    "Pineapple": "$3.50"
}


class Smoothie:
    # Write code here!
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        total_cost = 0
        for item in self.ingredients:
            cost = prices[item]
            cost = float(cost[1:len(cost)])
            total_cost += cost
        print(total_cost)
        total_cost = '{:.2f}'.format(total_cost)
        str_cost = "$" + str(total_cost)
        return str_cost

    def get_price(self):
        str_cost = self.get_cost()
        num_cost = float(str_cost[1:len(str_cost)])
        price = round(num_cost * 2.5, 2)
        price = '{:.2f}'.format(price)
        price = "$" + str(price)
        print(price)
        return price

    def get_name(self):
        ingreds = sorted(self.ingredients)
        if 'Strawberries' in ingreds:
            ingreds[ingreds.index('Strawberries')] = 'Strawberry'
        if 'Blueberries' in ingreds:
            ingreds[ingreds.index('Blueberries')] = 'Blueberry'
        if 'Raspberries' in ingreds:
            ingreds[ingreds.index('Raspberries')] = 'Raspberry'

        if len(ingreds) > 1:
            name_str = " ".join(ingreds) + " Fusion"
        else:
            name_str = " ".join(ingreds) + " Smoothie"

        return name_str


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        # Write code here!
        if self.age == other.age:
            str = '{} is the same age as me.'.format(other.name)

        if self.age < other.age:
            str = '{} is older than me.'.format(other.name)

        if self.age > other.age:
            str = '{} is younger than me.'.format(other.name)

        print(str)
        return str


def main():
    ingreds = ['Banana']
    s1 = Smoothie(ingreds)

    print(s1.ingredients)
    print(s1.get_cost())
    cost = s1.get_cost()
    print(s1.get_price())
    print(s1.get_name())
    print('test')


if __name__ == '__main__':
    main()
