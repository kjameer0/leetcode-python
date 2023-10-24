def ex_func():
    x = int(input('enter number 1'))
    y = int(input('enter number 2'))
    if (x * y >= 1000):
        return x * y
    else:
        return x + y


def for_loop():
    prev = 0
    for i in range(0, 10):
        print(i + prev)
        prev = i
    return 'done'


def num_pattern():
    num_string = ''
    for i in range(1, 6):
        num_string += str(i) + ' '
        print(num_string)


def all_sum():
    end = int(input('choose a number'))
    total = 0
    for i in range(1, end + 1):
        total += i
    return total


def times_table(num):
    for i in range(1, 13):
        print(num * i)


def five_div(list):
    for i in range(0, len(list)):
        cur = list[i]
        if cur > 500:
            break
        if cur % 5 != 0 or cur > 150:
            continue
        print(cur)


for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))


class Human:
    def __init__(self, style: str) -> None:
        self.style = style

    def get_name(self):
        print(f"I have {self.style} style")


x: int = 5
x = 'hi'
print(x)
bermaine = Human("nice")
bermaine.get_name()
print()
