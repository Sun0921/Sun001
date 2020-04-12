#! /usr/bin/env python3
#程序判断一个数是否小于一百
a = int(input("请输入一个数字判断是否小于一百："))
#首先输入数字
b = 100
#然后赋值b=100
if a < b:
    print("小于100")
#然后判断这个数字是否大于或小于100
elif a == b:
    print("等于100")
else:
    print("大于100")
