import functools

__author__ = "___Kalinina ___"
__copyright__ = "___Copyright 2018, Kalinina Ariana"
__email__ = "__rishkolin@gmail.com___"

def errorCheck(a):
    try:
        a = int(a)
    except ValueError:
        print("Invalid input, not an integer")
        return False
    if a in list(range (0, 10)):
        return True
    else:
        print("Input is not within the data range.")
        return False


def checked(f):
    """
    Decorator for number pre-checking
    """
    @functools.wraps(f)
    def checker(*args, **kwargs):
        if errorCheck(kwargs['number']):
            return f(*args, **kwargs)
        else:
            return False
    return checker

def converted(f):
    @functools.wraps(f)
    def converter(*args, **kwargs):
        basement = kwargs['basement']
        number = int(kwargs['number'])
        if basement==2:
            f(*args, **kwargs, result=bin(number)[2:])
        elif basement==8:
            f(*args, **kwargs, result=oct(number)[2:])
        elif basement==16:
            f(*args, **kwargs, result=hex(number)[2:])
        else:
            return None
    return converter

@converted
def print_result(basement, number, result):
    print(f"Result in {basement} is {number}")

def get_basement(type):
    if type=='bin':
        return 2
    elif type=='oct':
        return 8
    elif type=='hex':
        return 16
    else:
        return 0

@checked
def get_name(number):
    """
    Get the name of a digit
    :param number:
    :return:
    """
    a_dict = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four",5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    name = a_dict[int(number)]
    return name

if __name__ == '__main__':

    a = input()
    print(get_name(number=a))

    b = input()
    # b - basement of the number system
    if b in ['bin','oct','hex']:
        basement = get_basement(b)
        print_result(basement=basement, number=a)


#if (a>9):
#  print("Число больше 9. Введите еще раз.")
#  a = int(input())
#else: a=a
