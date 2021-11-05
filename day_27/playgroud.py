def add(*num):
    total = 0
    for n in num:
        total += n
    return total


print(add(5, 1, 2, 5, 6, 6, 4, 5, 4, 5, 6, 4, 5, 6, 8, 7, 9, 8))

print(add(1, 2))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    print((kwargs["add"]))

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GTR")
print(my_car.model)

my_new_to_me_car = Car()
print(my_new_to_me_car.model)

my_new_to_me_car = Car(make="Pore", model="You", seats="2")
print(my_new_to_me_car.colour)
