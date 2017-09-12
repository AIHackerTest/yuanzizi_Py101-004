"""
    升级版猜数字小游戏，实现以下功能：

    程序内部用 0-9 生成一个 4 位数，每个数位上的数字不重复，且首位数字不为零，如 1942
    用户输入 4 位数进行猜测，程序返回相应提示
        用 A 表示数字和位置都正确，用 B 表示数字正确但位置错误
        用户猜测后，程序返回 A 和 B 的数量
        比如：2A1B 表示用户所猜数字，有 2 个数字，数字、位置都正确，有 1 个数字，数字正确但位置错误
    猜对或用完 10 次机会，游戏结束
"""
import sys
import random

# ----- 以下是函数定义 ------------

# 初始化数组
def Initial_num(bits_num) :
    bits = ["0","1","2","3","4","5","6","7","8","9"] # 初始化数组
    num = random.sample (bits,bits_num) # 随即取出 bits_num 个数

    while num[0] == 0: # 判断第一位是否为0，如果是重新取
        num = random.sample (bits,bits_num)

    return num # 返回一个bits_num 位数的数组

# 初始化输入值
def Initial_Input_to_Type(promote='',bit_num=0,t='int'): # promote 为提示语，bit_num = 0 代表对输入的位数没有限制

    i = input(promote)
    while not Check_Input_num (i,bit_num)  :
        i = input(promote)
    else :
        return int(i)

# 校验input 是否有为数字和位数是否符合
def Check_Input_num (str,bit_num = 0): # bit_num = 0 代表对输入的位数没有限制
    if bit_num == 0 and  Check_Every_Bit_int(str) :
        return True
    elif len(str) == bit_num and  Check_Every_Bit_int(str):
        return True
    else :
        return False

# 校验input 是否有为数字和位数是否符合
def Check_Every_Bit_int(str) :
    flag = 0 # 位数校验通过计数器
    for bit in str:
            try: # 检测输入的异常
                int (bit)
                flag = flag +1
            except ValueError:
                print ("Some Error appear at %s with %s : " % (bit,sys.exc_info()[0]))
    if flag == len(str):
        return True
    else:
        return False


# 将input 转换为 int类型
def String_to_Int(str,bit = 0) : # bit = 0 代表对输入的位数没有限制
    if Check_Input_num (str,bit):
        return int(str)

# 遍历判断
def Check_Guess_Result(num,num_guess):
    a = 0
    b = 0
    bits_num = len (num)
    for i in range(bits_num):
#        print (i," :  ",num_guess[i])

        for j in range(bits_num):
#            print ("---j=",j," :  ",num[j])

            if num_guess[i] == num[j]:
                if i == j:
                    a = a+1
                else:
                    b = b+1

    print("The result: %d A %d B" % (a,b))
    return a



# 猜数函数
def Guess(num,times) :
    flag = 0
    print("-----Guess a [{}] bit number ! Are U Ready?-----".format(len(num)))
    for i in range(times):
        print("*** {} times ***: ".format(i+1),end='')
        num_guess = input()
        while not Check_Input_num (num_guess,len(num)): # 不符合输入条件，重新输入
            num_guess = input("请重新输入一个{}位数：".format(len(num)))

        if Check_Guess_Result(num,num_guess) == len(num) :
            print ("Congrutulation~! You're Right!")
            flag = 1
            break # 退出 for  循环

    if flag == 0:
        print("""
            ------------------------------------------------------------
            Petty,tims is out~!The correct number is {}"
            ------------------------------------------------------------
            """.format(num))


# ----- 以下是程序主体 ------------

bits_num = Initial_Input_to_Type("Please the bits you want to guess:",1,'int')
times = Initial_Input_to_Type("Please the times you want to guess:",0,'int')
num = Initial_num(bits_num)

Guess (num,times)
