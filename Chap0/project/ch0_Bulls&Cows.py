"""
    猜数字（又称 Bulls and Cows ）是一种古老的密码破译类益智小游戏，
    起源 20 世纪中期，一般由两人或多人玩。

    程序随机生成一个 20 以内的数字，用户有 10 次机会猜测
    程序根据用户输入，给予一定提示（大了、小了、正确）
    猜对或用完 10 次机会，游戏结束
"""
import random
import sys

num = random.randint(0,20)
flag = 0 # 猜中标志位
print( num )

print("Guess the number between 0 to 20! Are U Ready?")
for i in range( 10 ):
    #print( i )
    print("Please input the {} times number you guess:".format(i+1),end='')
    try:
        num_guess = int(input())
    except ValueError:
        print("Some Error appear: ",sys.exc_info()[0])
        flag = 2;
        break

    if num_guess == num:
        print ("Congrutulation~! You're Right!")
        flag = 1
        break
    elif num_guess > num:
        print ("You guess too large, Try again.")
    elif num_guess < num:
        print ("You guess too small, Try again.")

if flag == 0:
    print("Petty,tims is out~!The correct number is {}".format(num))
