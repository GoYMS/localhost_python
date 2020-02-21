import random

time = 3
runnum = random.randint(1, 13)
num = input("请你猜一个数字:")
number = int(num)

while time != 0:
    time = time - 1
    if number == runnum:
        print("猜对了")

    elif number < runnum:
        print("猜小了" + "你还有" + str(time) + "次机会")

    elif number > runnum:
        print("猜大了" + "你还有" + str(time) + "次机会")

    if time != 0:
        num = input("请你猜一个数字:")
        number = int(num)