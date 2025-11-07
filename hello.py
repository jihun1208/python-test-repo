print("hello world!")

numbers = [1,2,3]

def packing(*numbers):
    for number in numbers:
        print(number)
        print()
packing(*numbers)