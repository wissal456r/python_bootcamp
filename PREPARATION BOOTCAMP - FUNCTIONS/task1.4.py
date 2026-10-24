def bread():
    print("<//////////>")


def lettuce():
    print("~~~~~~~~~~~~")


def tomato():
    print("O O O O O O")


def ham():
    print("============")


def sandwich(vegetarian=False):
    bread()

    if vegetarian:
        lettuce()
        lettuce()
        tomato()
        tomato()
    else:
        lettuce()
        tomato()
        ham()
        ham()

    bread()


sandwich()
print("Vegetarian sandwich:")
sandwich(True)
