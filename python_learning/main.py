#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'this module used for python3 learning'

# import pdb
# import math
# import copy
# import time
# import sys
# import sklearn
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import functools
# from scipy import sparse
# from collections import Iterable
# from collections import Callable
# from IPython.display import display


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


# def fn(x, y):
#     return x*10+y


# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]


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


# def f(a,b):
#     if not isinstance(a,(int)):
#         raise TypeError
#     if not isinstance(b,(int)):
#         raise TypeError
#     return a+b


# class Person:
#     def __init__(self,name):
#         self.name=name

#     def introduce(self):
#         print('Hello, my name is {}'.format(self.name))


# class Engineer(Person):
#     def __init__(self,name,position):
#         self.position=position
#         Person.__init__(self,name)

#     def greet(self):
#         print('Hello, my name is {} and I am a {} engineer!'.format(self.name,self.position))


# def main():
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
# print(reduce(fn, map(char2num, '98765')))
# s='iloveyou'
# print(s[::-1])
# a=[1,2,3,4,5]
# aa=[a,a,a]
# print(aa)
# a.append(6)
# print(aa)
# a.pop()
# aa=[list(a),list(a),list(a)]
# a.append(6)
# print(aa)
# a=[1,2,3,4,5]
# print(id(a))
# aa=[a,a,a]
# print(id(aa[0]))
# bb=[list(a),list(a),list(a)]
# bb=[copy.copy(a),copy.copy(a),copy.copy(a)]
# print(id(bb[0]))
# a=100
# b=a
# print(id(a),id(b))
# a=[1,2,3]
# b=copy.deepcopy(a)
# print('a id is',id(a))
# print('b id is',id(b))
# print('a[0] id is',id(a[0]))
# print('b[0] id is',id(b[0]))
# a[0]=2
# b[0]=2
# print('a id is',id(a))
# print('b id is',id(b))
# print(id(a[0]))
# print(id(b[0]))
# print(id(a[1]))
# print(id(b[1]))
# print(id(1))
# a=[[1,2,3],[1,2,3],[1,2,3]]
# b=copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(a[0]))
# print(id(b[0]))
# b=copy.copy(a)
# print(id(a))
# print(id(b))
# print(id(a[0]))
# print(id(b[0]))
# a=(1,2,3)
# b=copy.copy(a)
# print(id(a))
# print(id(b))
# b=copy.deepcopy(a)
# print(id(a))
# print(id(b))
# a_string="abcde"
# print(a_string,end=',')
# print(a_string,end='\n')
# ddict={1:'123',2:'234',3:'345'}
# for idx,val in enumerate(ddict):
#     print(idx,val)
# a=input()
# for ch in a:
#     if ch>='a' and ch<='z':
#         print(chr(ord('a')+(ord(ch)-ord('a')+2)%26),end='')
#     else:
#         print(ch,end='')
# s1=set(range(3))
# s2=set(range(2,5))
# print(s1 & s2)
# print(s1 | s2)
# print(s1 - s2)
# print(s1 ^ s2)
# f=open('test2.txt',mode='x',encoding='utf8')
# f.write('this is just a test 2')
# f.flush()
# f.close()
# with open('test2.txt','r') as f:
#     for line in f:
#         print(line)
# print(f.__name__)
# print(f.__class__)
# print(f(b=2,a=1))
# a=[0,10,2]
# print(list(range(*a)))
# a=[4,3,2,1]
# print(sorted(a))
# a=list(range(0,10))
# print(list(filter(lambda x: x%2==0,a)))
# a=[4,3,2,1]
# print(tuple(map(lambda x: x*x,a)))
# a=list(range(0,6,1))
# filter_result=list(filter(lambda x: x%2==0,a))
# map_result=list(map(lambda x: x**x,a))
# reduce_result=reduce(lambda a,b: a+b,a,0)
# print("{}, {}, {}".format(filter_result,map_result,reduce_result))

# def analyze(line):
#     dict_of_result={}
#     list_of_line=list(line.split())
#     list_of_brand_name=[]
#     for index,value in enumerate(list_of_line):
#         if index==len(list_of_line)-1:
#             dict_of_result['size']=value
#         elif index==len(list_of_line)-2:
#             dict_of_result['brand']=' '.join(list_of_brand_name)
#             dict_of_result['color']=value
#         else:
#             list_of_brand_name.append(value)
#     return dict_of_result

# result=[]
# with open('test.txt','r') as f:
#     list_of_all_lines=f.readlines()
#     for current_line in list_of_all_lines:
#         result.append(analyze(current_line))
# result.sort(key=lambda elem: elem['size'])
# for element in result:
#     print(element)

# def time_fun(real_fun):
#     def wrapper():
#         print('start time: {}'.format(time.time()))
#         real_fun()
#         print('end time: {}'.format(time.time()))

#     return wrapper

# @time_fun
# def fun():
#     print('this is funny')

# fun()

# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             print("{} {}():".format(text,func.__name__))
#             return func(*args,**kwargs)
#         return wrapper
#     return decorator

# @log('execute')
# def now():
#     print("{}".format(time.time()))

# now()

# def addPrintLog(log):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             print("{} {}():".format(log,func.__name__))
#             return func(*args,**kwargs)
#         return wrapper
#     return decorator

# @addPrintLog('exec')
# def testFunc(times):
#     print('this function runs {} time(s)!'.format(times))

# testFunc(2)

# jack=Person('jack')
# print(dir(jack))
# jack=Engineer('jack','shenzhen')
# jack.greet()
# jack.introduce()

# def is_odd(n):
#     return n%2==1

# print(list(filter(is_odd,list(range(10)))))

# def add(a:int, b:int)->int:
#     return a+b

# print(add(1,2))

# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         n=len(word1)
#         m=len(word2)
#         dp=[]
#         for i in range(n+1):
#             dp.append([])
#             for j in range(m+1):
#                 dp[i].append(0)

#         for i in range(n+1):
#             dp[i][0]=i
#         for i in range(m+1):
#             dp[0][i]=i

#         for i in range(1,n+1):
#             for j in range(1,m+1):
#                 if word1[i-1]==word2[j-1]:
#                     dp[i][j]=dp[i-1][j-1]
#                 else:
#                     dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1

#         return dp[n][m]

# def not_empty(s:list):
#     return s and s.strip()

# print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

# python 欧拉筛
# def odd_iter():
#     n=1
#     while True:
#         n=n+2
#         yield n

# def not_divisible(n):
#     return lambda x: x%n>0

# def getPrime():
#     yield 2
#     it=odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it=filter(not_divisible(n),it)

# for i in getPrime():
#     if i<1000:
#         print("{}".format(i),end=' ')
#     else:
#         break

# a=list(range(-10,10,2))
# print(sorted(a,key=abs,reverse=False))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# def calc_sum(*args):
#     ret=0
#     for i in args:
#         ret=ret+i
#     return ret

# print(calc_sum(*list(range(1,11,1))))

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs=[]
#     for i in range(1,4):
#         fs.append(f(i))
#     return fs

# f1,f2,f3=count()
# print(f1())
# print(f2())
# print(f3())

# def createCounter():
#     def generator():
#         a=1
#         yield a
#         while True:
#             a+=1
#             yield a

#     g=generator()

#     def counter():
#         return next(g)

#     return counter

# cnt=createCounter()
# for i in range(1,11,1):
#     print(cnt())

# print(list(map(lambda x: x**2,list(range(1,10)))))

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('call {}():'.format(func.__name__))
#         return func(*args, **kwargs)
#     return wrapper

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print('{} {}():'.format(text, func.__name__))
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# @log('exec')
# def f(a, b, c):
#     return max(a, b, c)

# print(f(1, 2, 3))

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         matrix2 = []
#         for i in range(n):
#             matrix2.append([])
#         for i in range(n-1, -1, -1):
#             for j in range(n):
#                 matrix2[j].append(matrix[i][j])

#         matrix[:] = matrix2[:]

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{} * {} = {}".format(i, j, i*j), end='  ')
#     print(end='\n')

# temperature = input('Please input the temperature, such as 100C or 128F: ')
# try:
#     # input format check
#     if temperature == '' or len(temperature) == 1:
#         raise ValueError('Input format error!')
#     # convert input
#     temperatureUnit = temperature[-1].upper()
#     temperature = float(temperature[:-1])
#     # temperature unit check
#     if temperatureUnit != 'C' and temperatureUnit != 'F':
#         raise ValueError('Temperature unit is wrong!')
#     # calculate and print answer
#     if temperatureUnit == 'C':
#         temperature = temperature*1.8+32
#         temperatureUnit = 'F'
#     else:
#         temperature = (temperature-32)/1.8
#         temperatureUnit = 'C'
#     print('It equals to {}{}'.format(temperature, temperatureUnit))

# except ValueError as ve:
#     print('Error:', ve)

# finally:
#     print('Program finished.')

# a = 1
# b = 1
# c = a
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(1))
# 以上结果相同

# n = 3
# dp = [0]*n
# dp = dp*n
# print(dp)

# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         dp = [0]*(K+1)
#         cnt = 0
#         while (dp[K] < N):
#             cnt += 1
#             for i in range(K, 0, -1):
#                 dp[i] += dp[i-1]+1
#         return cnt

# n = 3
# a = [[] * n for i in range(n)]
# aa = [a for i in range(n)]
# print(aa)

# int2 = functools.partial(int, base=2)
# print(int2('10'))
# print(int2('10', base=10))

# class Student(object):
#     name = 'global name'

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def getInfo(self):
#         print(self.__name, self.__score)

# def printClassInfo():
#     print('this is just a test')


# def main():
#     s1 = Student('Tom', 100)
#     s1.getInfo()
# Student.printClassInfo()
# print(s1._Student__name) // not recommend

# def main():
# print(dir(Student))
# s1 = Student('Tom', 100)
# print(getattr(s1, 'name'))

# from types import MethodType


# def set_age(self, age):
#     self.age = age


# def get_age(self):
#     return self.age


# class Student(object):
#     __slots__ = ('name', 'age', 'set_age', 'get_age')

#     def __init__(self, age):
#         self.age = age


# def main():
#     s1 = Student(10)
#     s1.set_age = MethodType(set_age, s1)
#     s1.get_age = MethodType(get_age, s1)
#     s1.set_age(20)
#     print(s1.get_age())
#     s1.name = 'Tom'
#     s1.score = 99
#     print(s1.score)

# class Student(object):
#     def __init__(self, score):
#         self.__score = score

#     @property
#     def score(self):
#         return self.__score

#     @score.setter
#     def score(self, score):
#         if not isinstance(score, int):
#             raise ValueError('not int!')
#         if score < 0 or score > 100:
#             raise ValueError('range error!')
#         self.__score = score


# def main():
#     s = Student(10)
#     s.score = 20
#     print(s.score)

# class A(object):
#     a = 0


# class B(A):
#     pass


# class C(A):
#     pass


# class D(B, C):
#     pass


# def main():
#     d = D()
#     print(d.a)

# class Base:
#     def __init__(self):
#         print('Base.__init__')


# class A(Base):
#     def __init__(self):
#         super().__init__()  # 1
#         print('A.__init__')


# class B(Base):
#     def __init__(self):
#         super().__init__()  # 2
#         print('B.__init__')


# class C(A, B):
#     def __init__(self):
#         super().__init__()  # 3
#         print('C.__init__')

# class Student(object):
#     def __init__(self, name):
#         self.__name = name

#     def __str__(self):
#         return 'This student \'s name is {}'.format(self.__name)

#     __repr__=__str__


# def main():
#     s = Student('Tom')
#     print(s)


# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a

#     def __getitem__(self, n):
#         a, b = 0, 1
#         if isinstance(n, int):
#             for x in range(n):
#                 a, b = b, a+b
#             return a
#         elif isinstance(n, slice):
#             start, stop = n.start, n.stop
#             if start == None:
#                 start = 0
#             ret = []
#             for i in range(stop):
#                 if i >= start:
#                     ret.append(a)
#                 a, b = b, a+b
#             return ret

# class Student(object):
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print('My name is {}'.format(self.name))

# def main():
# for i in Fib():
#     print(i, end=' ')
# print(Fib()[5])
# print(Fib()[5:10])
# s = Student('Tom')
# s()

# from enum import Enum


# def main():
#     Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
#                            'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#     for name, member in Month.__members__.items():
#         print(name, '=>', member, ',', member.value)

# from enum import Enum, unique

# @unique
# class Weekly(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6


# def main():
#     print(Weekly.Mon)

# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, {}'.format(name))


# def main():
# def fn(self, name='world'):
#     print('Hello, {}'.format(name))

# Hello = type('Hello', (object,), dict(hello=fn))
# h = Hello()
# h.hello()

# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)

# class MyList(list, metaclass=ListMetaclass):
#     pass

# def main():
#     l = MyList()
#     l.append(1)
#     print(l)

# using metaclass in databases coding

# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type

#     def __str__(self):
#         return '<{}:{}>'.format(self.__class__, self.name)


# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')


# class IntegerField(Field):
#     def __init__(self, name):
#         super(IntegerField, self).__init__(name, 'bigint')


# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: {}'.format(name))
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: {} ==> {}'.format(k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings
#         attrs['__table__'] = name
#         return type.__new__(cls, name, bases, attrs)


# class Model(dict, metaclass=ModelMetaclass):
#     def __init__(self, **kwargs):
#         super(Model, self).__init__(**kwargs)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(
#                 r"'Model' object has no attribute '{}'".format(key))

#     def __setattr__(self, key, value):
#         self[key] = value

#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into {} ({}) values ({})'.format(
#             self.__table__, ','.join(fields), ','.join(params))
#         print('SQL: {}'.format(sql))
#         print('ARGS: {}'.format(args))


# class User(Model):
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')


# def main():
#     u = User(id=1234, name='Michael', email='test@test.com', password='my-pwd')
#     u.save()

# import logging

# def foo(s):
#     return 10/int(s)

# def bar(s):
#     return foo(s)*2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10/n

# def main():
#     foo('0')

# import logging
# logging.basicConfig(level=logging.INFO)

# def main():
#     s = '0'
#     n = int(s)
#     pdb.set_trace()
#     logging.info('n = {}'.format(n))
#     print(10/n)

# import unittest

# class Dict(dict):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(
#                 r"'Dict' object has no attribute '{}'".format(key))

#     def __setattr__(self, key, value):
#         self[key] = value

# class TestDict(unittest.TestCase):
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))

#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')

#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')

#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']

#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty

# from io import StringIO

# def main():
#     f = StringIO()
#     f.write('hello\nhello\n')
#     print(f.getvalue())

# import os

# def main():
# print(os.environ)
# print(os.path.abspath('.'))
# print(os.path.join('c:\\ProgramFiles', 'testdir'))
# print(os.path.split('c:\\ProgramFiles\\test.txt'))
# print(os.path.splitext('c:\\ProgramFiles\\test.txt'))
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(
#     x) and os.path.splitext(x)[1] == '.py'])

# import pickle

# def main():
#     d = dict(name='bob', age=20, score=80)
# pickle.dumps(d)

# import json

# def main():
#     d = dict(name='bob', age=20, score=80)
#     print(json.dumps(d))

# import os

# def main():
#     print('Process {} start...'.format(os.getpid()))
#     pid = os.fork()
#     if (pid == 0):
#         print('I am child process {} and my parent is {}'.format(
#             os.getpid(), os.getppid()))
#     else:
#         print('I am {} and my child is {}'.format(os.getpid(), pid))

# from multiprocessing import Process
# import os

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# def main():
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def main():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


if __name__ == '__main__':
    main()
    # unittest.main()

# print('END')
