#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
    a = input().split(' ')
    a = [int(a[i]) for i in range(len(a))]
    print(a)


if __name__ == '__main__':
    main()
