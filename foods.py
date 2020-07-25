class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food):
        result_str = ''
        if food in self.likes:
            result_str = '{} eats the {} and loves it!'.format(self.name, food)

        elif food in self.hates:
            result_str = '{} eats the {} and hates it!'.format(self.name, food)

        elif (food not in self.hates) & (food not in self.likes):
            result_str = '{} eats the {}!'.format(self.name, food)

        return result_str


def main():
    p1 = Person("Sam", ["ice cream", "pie", "apples"], ["carrots", "bananas", "cheese", "lettuce"])
    p2 = Person("Mitchell", [], ["brocolli", "lettuce", "cheese", "pie", "apples", "bananas", "ice cream", "carrots"])
    p3 = Person("Julie", ["brocolli", "lettuce", "cheese", "pie", "apples", "bananas", "ice cream", "carrots"], [])
    p4 = Person("Steven", [], [])
    p5 = Person("Joshua", ["ice cream", "pie", "cheese", "bananas"], ["lettuce", "apples"])

    # Evaluate test cases
    assert (p1.taste("ice cream") == "Sam eats the ice cream and loves it!")
    assert (p1.taste("carrots") == "Sam eats the carrots and hates it!")
    assert (p1.taste("brocolli") == "Sam eats the brocolli!")
    assert (p1.taste("lettuce") == "Sam eats the lettuce and hates it!")
    assert (p1.taste("cheese") == "Sam eats the cheese and hates it!")
    assert (p1.taste("pie") == "Sam eats the pie and loves it!")
    assert (p1.taste("apples") == "Sam eats the apples and loves it!")
    assert (p1.taste("bananas") == "Sam eats the bananas and hates it!")
    assert (p2.taste("ice cream") == "Mitchell eats the ice cream and hates it!")
    assert (p2.taste("carrots") == "Mitchell eats the carrots and hates it!")
    assert (p2.taste("brocolli") == "Mitchell eats the brocolli and hates it!")
    assert (p2.taste("lettuce") == "Mitchell eats the lettuce and hates it!")
    assert (p2.taste("cheese") == "Mitchell eats the cheese and hates it!")
    assert (p2.taste("pie") == "Mitchell eats the pie and hates it!")
    assert (p2.taste("apples") == "Mitchell eats the apples and hates it!")
    assert (p2.taste("bananas") == "Mitchell eats the bananas and hates it!")
    assert (p3.taste("ice cream") == "Julie eats the ice cream and loves it!")
    assert (p3.taste("carrots") == "Julie eats the carrots and loves it!")
    assert (p3.taste("brocolli") == "Julie eats the brocolli and loves it!")
    assert (p3.taste("lettuce") == "Julie eats the lettuce and loves it!")
    assert (p3.taste("cheese") == "Julie eats the cheese and loves it!")
    assert (p3.taste("pie") == "Julie eats the pie and loves it!")
    assert (p3.taste("apples") == "Julie eats the apples and loves it!")
    assert (p3.taste("bananas") == "Julie eats the bananas and loves it!")
    assert (p4.taste("ice cream") == "Steven eats the ice cream!")
    assert (p4.taste("carrots") == "Steven eats the carrots!")
    assert (p4.taste("brocolli") == "Steven eats the brocolli!")
    assert (p4.taste("lettuce") == "Steven eats the lettuce!")
    assert (p4.taste("cheese") == "Steven eats the cheese!")
    assert (p4.taste("pie") == "Steven eats the pie!")
    assert (p4.taste("apples") == "Steven eats the apples!")
    assert (p4.taste("bananas") == "Steven eats the bananas!")
    assert (p5.taste("ice cream") == "Joshua eats the ice cream and loves it!")
    assert (p5.taste("carrots") == "Joshua eats the carrots!")
    assert (p5.taste("brocolli") == "Joshua eats the brocolli!")
    assert (p5.taste("lettuce") == "Joshua eats the lettuce and hates it!")
    assert (p5.taste("cheese") == "Joshua eats the cheese and loves it!")
    assert (p5.taste("pie") == "Joshua eats the pie and loves it!")
    assert (p5.taste("apples") == "Joshua eats the apples and hates it!")
    assert (p5.taste("bananas") == "Joshua eats the bananas and loves it!")


if __name__ == '__main__':
    main()
