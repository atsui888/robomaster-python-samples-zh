for 次数 in range(1, 360):
    print("    弧度 = 数学.弧度(" + str(次数) + ")\n    " +
        "积 *= 数学.正弦(弧度)**2 + 数学.余弦(弧度)**2")
    #print("    结果 = 算三角函数()")