def add(*args):
    print(args[0])
    sum = 0
    for num in args:
        sum += int(num)
    return sum


print(add(2,3,2,3,4,2))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, val in kwargs.items():
    #     print(key, val)
    print(kwargs['add'])
    n += kwargs['add']

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.coolness = kwargs.get("10/10")


Fucking_Car = Car(make="Nissan", model="GT-R", color="blue")
print(Fucking_Car.color)