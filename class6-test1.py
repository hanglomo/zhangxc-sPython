a=1
while a<=1000:
    print("我是天才")
    a=a+1


#一百以内所有偶数的和
a=1
b=0
while a<=100:
    a=a+1
    b=b+a
print("一百以内所有偶数的和",b)


a=1
b=0
while a<=100:
    if a%2==0:
        b=b+a
    a=a+1
print("偶数",b)


#猜字游戏

import random

g=random.randint(1,10)
a=int(input("你猜猜"))
i=1
while a!=g:
    if a>g:
        print("大了")
    else:
        print("小了")
    a=int(input("你再猜猜"))
    i+=1
print("猜对了","真棒")
print("一共猜对了{}次".format(i))
