print('hello world')


def square_counter():
    a = int(input("Įveskite skaičių: "))
    p = a*a
    return p


def password_entering():
    pw = 0
    while pw != 854:
        pw = int(input("Įveskite slaptažodį: "))
    print('Code accepted')


def decimal_to_binary(d):
    binary_string = ''
    while d != 0:
        r = d % 2
        if r == 1:
            binary_string = '1' + binary_string
        else:
            binary_string = '0' + binary_string
        d = int(d) / 2
    return binary_string

print(decimal_to_binary(18))


def greatest_common_divisor():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(a)

