sweet_dict = {
    'Plain': 0
    , 'Vanilla': 5
    , 'ChocolateChip': 5
    , 'Strawberry': 10
    , 'Chocolate': 10
}


class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles


def sweetest_icecream(lst):
    output_list = []
    for obj in lst:
        if obj.flavor in sweet_dict.keys():
            sweetness = sweet_dict[obj.flavor] + obj.num_sprinkles
            output_list.append(sweetness)
    max_sweetness = max(output_list)
    return max_sweetness


def main():
    ice1 = IceCream("Chocolate", 13)
    ice2 = IceCream("Vanilla", 0)
    ice3 = IceCream("Strawberry", 7)
    ice4 = IceCream("Plain", 18)
    ice5 = IceCream("ChocolateChip", 3)
    ice6 = IceCream("Chocolate", 23)
    ice7 = IceCream("Strawberry", 0)
    ice8 = IceCream("Plain", 34)
    ice9 = IceCream("Plain", 81)
    ice10 = IceCream("Vanilla", 12)

    assert (sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) == 23)
    assert (sweetest_icecream([ice7, ice10, ice1, ice6, ice8, ice10, ice2, ice2]) == 34)
    assert (sweetest_icecream([ice10, ice10, ice6, ice8, ice4]) == 34)
    assert (sweetest_icecream([ice2, ice10, ice6, ice9, ice7]) == 81)
    assert (sweetest_icecream([ice10, ice6, ice4, ice1, ice7, ice8, ice6]) == 34)
    assert (sweetest_icecream([ice3, ice1]) == 23)
    assert (sweetest_icecream([ice6, ice7, ice5, ice4, ice3]) == 33)
    assert (sweetest_icecream([ice4, ice8, ice9]) == 81)
    assert (sweetest_icecream([ice5, ice7]) == 10)
    assert (sweetest_icecream([ice5, ice3, ice6, ice2, ice7, ice2, ice7, ice2]) == 33)
    assert (sweetest_icecream([ice1, ice9, ice10, ice9, ice7, ice1, ice9]) == 81)
    assert (sweetest_icecream([ice1, ice4]) == 23)
    assert (sweetest_icecream([ice7, ice4]) == 18)
    assert (sweetest_icecream([ice1, ice8, ice6, ice7, ice3, ice2, ice3, ice7]) == 34)
    assert (sweetest_icecream([ice7, ice8, ice4, ice4, ice5, ice1]) == 34)
    assert (sweetest_icecream([ice10, ice10, ice9, ice4, ice7, ice9]) == 81)
    assert (sweetest_icecream([ice3, ice10, ice1]) == 23)
    assert (sweetest_icecream([ice3, ice4, ice7, ice3, ice7, ice10, ice2]) == 18)
    assert (sweetest_icecream([ice5, ice9, ice9, ice9, ice7, ice5, ice9, ice7]) == 81)
    assert (sweetest_icecream([ice4, ice9, ice2]) == 81)
    assert (sweetest_icecream([ice8, ice2, ice2, ice2, ice4, ice8]) == 34)
    assert (sweetest_icecream([ice4, ice9, ice4, ice3, ice3, ice2, ice5, ice2]) == 81)
    assert (sweetest_icecream([ice8, ice10, ice5]) == 34)
    assert (sweetest_icecream([ice10, ice3, ice2, ice1, ice9]) == 81)
    assert (sweetest_icecream([ice8, ice3, ice4, ice5]) == 34)
    assert (sweetest_icecream([ice10, ice8, ice6, ice7, ice9, ice4]) == 81)
    assert (sweetest_icecream([ice5, ice4, ice6, ice6, ice1]) == 33)
    assert (sweetest_icecream([ice6, ice8, ice2, ice10, ice7, ice10]) == 34)
    assert (sweetest_icecream([ice1, ice9, ice7, ice3]) == 81)
    assert (sweetest_icecream([ice7, ice1, ice9, ice6, ice7, ice10, ice2, ice3]) == 81)
    assert (sweetest_icecream([ice5, ice1, ice7, ice6, ice8, ice1, ice8]) == 34)
    assert (sweetest_icecream([ice10, ice9, ice2, ice4, ice10]) == 81)
    assert (sweetest_icecream([ice3, ice7, ice10]) == 17)
    assert (sweetest_icecream([ice10, ice5, ice4]) == 18)
    assert (sweetest_icecream([ice9, ice2, ice4, ice8, ice3, ice3]) == 81)
    assert (sweetest_icecream([ice6, ice3, ice9, ice8, ice2, ice6]) == 81)
    assert (sweetest_icecream([ice10, ice3]) == 17)
    assert (sweetest_icecream([ice10, ice7, ice5, ice2, ice9]) == 81)
    assert (sweetest_icecream([ice10, ice10, ice4, ice1, ice9]) == 81)
    assert (sweetest_icecream([ice9, ice2, ice6, ice4, ice10, ice3]) == 81)
    assert (sweetest_icecream([ice8, ice10, ice1, ice7, ice8, ice9, ice1]) == 81)
    assert (sweetest_icecream([ice7, ice5, ice3, ice8, ice1, ice9]) == 81)
    assert (sweetest_icecream([ice2, ice6, ice3]) == 33)
    assert (sweetest_icecream([ice6, ice6]) == 33)
    assert (sweetest_icecream([ice9, ice6, ice8, ice3, ice2, ice2]) == 81)
    assert (sweetest_icecream([ice1, ice3, ice3, ice6]) == 33)
    assert (sweetest_icecream([ice8, ice6]) == 34)
    assert (sweetest_icecream([ice1, ice1]) == 23)
    assert (sweetest_icecream([ice4, ice2, ice3, ice9, ice5, ice10, ice6]) == 81)
    assert (sweetest_icecream([ice10, ice8, ice4, ice3, ice9, ice8, ice1, ice10]) == 81)
    assert (sweetest_icecream([ice5, ice8, ice5]) == 34)

    print('program execution complete...')




if __name__ == '__main__':
    main()
