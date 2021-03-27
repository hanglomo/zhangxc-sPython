   #计算儿子的身高
   m=int(input("请输入父亲的身高："))
   n=int(input("请输入母亲的身高："))
   p=n+m
   p=p*0.54
   print("儿子的身高是：",p)





  #计算柳树的数量
   a=int(input("请输入杨树的数量："))
   b=a*2
   c=b+4
   print("一共棵柳树",c)

  #计算可以买多少足球，剩余多少钱
   q=int(input("光头强带了多少钱："))
   w=int(input("一个足球多少钱："))
   e=q/w
   r=q%w
   print("一共买了",int(e))
   print("还有",r)


  #利用Turtle画图画一个金箍棒
   import turtle as a
   a.shape('turtle')
   a.pensize(10)
   a.color('yellow')
   a.forward(100)
   a.pensize(5)
   a.color('red')
   a.forward(200)
   a.pensize(10)
   a.color('yellow')
   a.forward(100)
