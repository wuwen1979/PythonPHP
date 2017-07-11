#coding=utf-8

def sayHello():
    print("你好")
    print("hello,world")
sayHello()


def sayHi(x):
    if x=='dog':
        print("wangwang!")
    elif x=='cat':
        print("miao,miao")
sayHi('dog')

def sayHi():
    global x
    print("x is ",x)
x=50
sayHi()


