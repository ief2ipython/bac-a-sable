#!/user/bin/env python3

import timeit


def first():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    squares_comprehension = [x**2 for x in a]
    #print(squares_comprehension)

def second():
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    square_lambda = list(map(lambda x: x ** 2, b))
    #print(square_lambda)


is_first  = (min(timeit.repeat(first)))
is_second = (min(timeit.repeat(second)))
print (is_first,is_second,is_second/is_first)

#if __name__ == '__main__':
#    first()
#   second()