    #复习
    s="1234567890"
    s.upper()
    s.lower()
    len(s)
    print(s【4】)



    s="我爱妈妈"
    a=print(s[:-3])
    z=print(s[2:])



    #字符串的截取
    a="PyThon的学习成果今天检测"
    b=a[-4:]
    c=a[:-4]
    e=b+c
    print(e)


    print("我叫{}，很厉害".format("张小成"))



    #占位符
    a=input()
    b=input()
    print("至高无{}，{}底捞针".format(a,b))



    #对齐方式的使用
    print("{:^7}".format("静夜思"))
    print("{:>7}".format("李白"))
    print("{:<7}".format("床前明月光，"))
    print("{:<7}".format("疑是地上霜。"))
    print("{:<7}".format("举头望明月，"))
    print("{:<7}".format("低头思故乡。"))
