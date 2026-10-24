def bread():
    print("<//////////>")


def lettuce():
    print("~~~~~~~~~~~~")


def tomato():
    print("O O O O O O")


def ham():
    print("============")


def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()


def make_sandwiches(number):
    if not isinstance(number, int) or isinstance(number, bool) or number < 0:
        print("I can't do this!")
        return

    for _ in range(number):
        sandwich()


make_sandwiches(2)
make_sandwiches(3.14)
