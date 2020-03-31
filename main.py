#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
# from collections import Iterable


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
    print([x*x for x in range(1, 11) if x & 1 == 1])


if __name__ == '__main__':
    main()
