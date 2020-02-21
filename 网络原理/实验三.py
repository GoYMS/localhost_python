"""
第一个


class Fruit:
    def beauty(self):
        print("美容养颜")
#雪梨
class SnowPear(Fruit):
    def cough(self):
        print("止咳")

class Apple(Fruit):
    # 颜色
    def color(self, color):
        self.color = color
    # 赠送
    def gift(self):
        if self.color == "红色":
            print("可以赠送")
        else:
            print("不能赠送")

color = str(input("苹果颜色为(红色或青色):"))
apple = Apple()
apple.color(color)
apple.beauty()
apple.gift()
"""

import os

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print("目录创建成功")
        print("文件成功存入")
        return True
    else:
        print("目录已存在")

        return False
# 创建文件
path = r"D:\tmp\test"
mkdir(path)
full_path = path + r"\练习.txt"
file = open(full_path, "w+", encoding='UTF-8')
file.write("《送孟浩然之广陵》\n年代: 唐\n作者: 李白\n故人西辞黄鹤楼，烟花三月下扬州。\n孤帆远影碧空尽，唯见长江天际流。")
file.close()
#读取文件
