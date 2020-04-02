#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from scipy import sparse
# from collections import Iterable
# from collections import Callable
from IPython.display import display


# def myAbs(number):
#     if not isinstance(number, (int, float)):
#         raise TypeError('bad operand type')
#     if number >= 0:
#         return number
#     else:
#         return -number


# def move(x, y, step, angle=0):
#     nx = x+step*math.cos(angle)
#     ny = y-step*math.sin(angle)
#     return nx, ny


# def power(number, pow=2):
#     ret = 1
#     base = number
#     while pow > 0:
#         if pow & 1 != 0:
#             ret = ret*base
#         base = base*base
#         pow = pow//2
#     return ret


# def enroll(name, age, gender='F', city='guangzhou'):
#     if not isinstance(name, (str)):
#         raise TypeError('Name type error')
#     if not isinstance(age, (int)):
#         raise TypeError('Age type error')
#     if not isinstance(gender, (str)):
#         raise TypeError('Gender type error')
#     if not isinstance(city, (str)):
#         raise TypeError('City type error')
#     print(name, age, gender, city)


# def add_end(a=[]):
#     a.append('end')
#     return a


# def add_end(a=None):
#     if a is None:
#         a = []
#     a.append('end')
#     return a


# def getSum(numbers):
#     sum = 0
#     for number in numbers:
#         sum += number
#     return sum

# def getSum(*numbers):
#     sum = 0
#     for number in numbers:
#         sum += number
#     return sum

# def personInfo(name, age, **extraArgs):
#     print('name =', name)
#     print('age =', age)
#     print('other =', extraArgs)

# def personInfo(name, age, *, city, job):
#     print(name, age, city, job)


# def personInfo(name, age, *args, city='beijing', job):
#     print(name, age, args, city, job)


# def niubiF(a, b, c=0, *args, d, **kw):
#     print(a, b, c, args, d, kw)


# def fact(number, ans=1):
#     if not isinstance(number, (int)):
#         raise TypeError('Number type error')
#     if number == 1:
#         return ans
#     else:
#         return fact(number-1, ans*number)


# def check(s):
#     if not isinstance(s, (str)):
#         raise TypeError
#     a = s[0:1]
#     b = s[-1:]
#     if a == ' ':
#         return check(s[1:])
#     elif b == ' ':
#         return check(s[:-1])
#     return s


# def fib(num):
#     n, a, b = 0, 0, 1
#     while n < num:
#         # print(b)
#         yield b
#         a, b = b, a+b
#         n = n+1
#     return 'done'


def fn(x, y):
    return x*10+y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


# def f(x):
#     return x*x


# def YHtri(line):
#     yield [1]
#     yield [1, 1]
#     pre = [1, 1]
#     j = 3
#     while j <= line:
#         now = [1, ]
#         i = 0
#         while i <= len(pre)-2:
#             now.append(pre[i]+pre[i+1])
#             i = i+1
#         now.append(1)
#         yield now
#         pre = now
#         j = j+1
#     return 'Done'


def main():
    # a, b = input().split(' ')
    # a = int(a)
    # b = int(b)
    # if a >= 0:
    #     print(a+b)
    # else:
    #     print(a-b)
    # print('I\'m Okay')
    # print('''Just
    # test
    # huanhang
    # ''')
    # a = input()
    # a = chr(ord(a)+65-97)
    # print(a)
    # print(len(b'ABC'))
    # print('中文'.encode('utf-8'))
    # a, b = input().split(' ')
    # a = int(a)
    # b = int(b)
    # print('The sum of a and b is %d.' % (a + b))
    # print('The sum of a and b is {0}'.format(a+b))
    # a = input().split(' ')
    # a = [int(a[i]) for i in range(len(a))]
    # print(a)
    # age = 16
    # print('your age is %d' % (age))
    # if age > 18:
    #     print('u r an adult')
    # elif age > 14:
    #     print('u r a teenager')
    # else:
    #     print('u r a child')
    # a = input().split(' ')
    # sum = 0
    # for i in a:
    #     i = int(i)
    #     sum += i
    # print(sum)
    # sum = 0
    # for i in list(range(101)):
    #     sum += i
    # print(sum)
    # ddict = {}
    # ddict['one'] = 1
    # ddict['two'] = 2
    # ddict[3] = 'three'
    # if 'one' in ddict:
    #     print(ddict['one'])
    # if 'two' in ddict:
    #     print(ddict['two'])
    # if 'three' in ddict:
    #     print(ddict[3])
    # print(ddict.get('three', -1))
    # ddict.pop('one')
    # if 'one' in ddict:
    #     print(ddict['one'])
    # ddict['one'] = 1
    # if 'one' in ddict:
    #     print(ddict['one'])
    # print(ddict)
    # ddict.pop(3)
    # ddict[3] = 'three'
    # print(ddict)
    # s1 = set(list(range(11)))
    # s2 = set(list([6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    # print(s1 | s2)
    # print(s2 - s1)
    # str1 = 'abca'
    # str2 = str1.replace('a', 'A')
    # print(str2)
    # s = set(list((1, [2, 3])))
    # print(s)
    # print(abs(-1))
    # print(max(3, 5, 6, 8, -1))
    # print(int(12.34))
    # print(int(12.54))
    # print(bool(1))
    # print(bool(0))
    # print(bool(-1))
    # a = int(input())
    # print(myAbs(a))
    # print(move(100, 100, 60, math.pi/6))
    # print(power(2, 10))
    # print(power(2))
    # enroll('Tom', 1, 'Boy')
    # enroll('Jelly', 2, city='beijing')
    # print(add_end())
    # print(add_end())
    # print(add_end())
    # print(getSum(1, 2, 3, 4))
    # a = (2, 3, 4, 5)
    # print(getSum(*a))
    # personInfo('Tom', 18, city='guangzhou', job='programmer')
    # personInfo('Tom', 18, 1, 2, 3, job='programmer', other='test')
    # niubiF(1, 2, 0, 1, 2, 3, k=1, d=1)
    # print(fact(1000))
    # a = list(range(10))
    # a.reverse()
    # print(a[-8:-5:2])
    # print(check('    12313 123132  '))
    # ddict = {'a': 1, 'c': 3, 'b': 2}
    # for key, val in ddict.items():
    #     print(key, val)
    # print(isinstance(ddict, (Iterable)))
    # a = list(range(10))
    # for key, val in enumerate(a, 1):
    #     print(key, val)
    # print([x*x for x in range(1, 11) if x & 1 == 1])
    # print([m+n for m in 'ABC' for n in 'XYZ'])
    # s = ['ABC', 'DIF', 'WE', 'WER']
    # print([i.lower() for i in s])
    # print([x if x % 2 == 0 else -x for x in range(1, 11)])
    # L1 = ['Hello', 'World', 18, 'Apple', None]
    # print([x for x in L1 if isinstance(x, (str))])
    # gen = (x*x for x in range(1, 11))
    # print([n for n in gen])
    # fib(10)
    # for n in fib(10):
    #     print(n)
    # for n in YHtri(10):
    #     print(n)
    # s = set([x*x for x in range(10)])
    # s2 = set([x for x in range(10)])
    # print(s | s2)
    # print(isinstance([], Iterable))
    # print(isinstance((), Iterable))
    # print(isinstance({}, Iterable))
    # print(isinstance('', Iterable))
    # print(isinstance(set([]), Iterable))
    # x = np.array([[1, 2, 3], [4, 5, 6]])
    # print("x:\n{}".format(x))
    # eye = np.eye(4)
    # print("This is eye in NumPy.\n{}".format(eye))
    # sparse_matrix = sparse.csr_matrix(eye)
    # print("This is eye_csr.\n{}".format(sparse_matrix))
    # row_indices = np.arange(4)
    # col_indices = np.arange(4)
    # data = np.ones(4)
    # eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
    # print("This is eye_coo.\n{}".format(eye_coo))
    # row_ptr = [0, 1, 2, 3, 4]
    # col = [0, 1, 2, 3]
    # data = [1, 1, 1, 1]
    # csr = sparse.csr_matrix((data, col, row_ptr))
    # print("Test{}".format(csr))
    # x = np.linspace(-10, 10, 100)
    # y = np.sin(x)
    # plt.plot(x, y, marker="x")
    # plt.show()
    # data = {
    #     'Name': ["John", "Anna", "Peter", "Linda"],
    #     'Location': ["New York", "Paris", "Berlin", "London"],
    #     'Age': [24, 13, 53, 33]
    # }
    # data_pandas = pd.DataFrame(data)
    # display(data_pandas)
    # print("{}".format(sklearn.__version__))
    # g = iter([1, 2, 3, 4, 5, 6])
    # print([n for n in g])
    # result = map(f, [x for x in range(10)])
    # print([i for i in result])
    # a = list(map(int, input().split(' ')))
    # print(a)
    print(reduce(fn, map(char2num, '98765')))


if __name__ == '__main__':
    main()
