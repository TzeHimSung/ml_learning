#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def myAbs(number):
    if not isinstance(number, (int, float)):
        raise TypeError('bad operand type')
    if number >= 0:
        return number
    else:
        return -number


def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


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
    print(move(100, 100, 60, math.pi/6))


if __name__ == '__main__':
    main()
