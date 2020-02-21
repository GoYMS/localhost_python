import random
import tkinter

#定义关于球的类
class RandomBall():
    #自动初始化画布和屏幕尺寸
    #canvas(结构化的图形，用于绘制图形，创建图形编辑器以及实现自定制的小构件类)
    def __init__(self,canvas,scrnwidth,scrnheight):
        #canvas:画布，
        #scrnwidth，scrnheight，屏幕宽高
        #初始化一个画布
        self.canvas = canvas
        #定义一个球的初始化位置，此位置为球的球心，位置随机
        self.xpos=random.randint(60,int(scrnwidth-60))
        self.ypos=random.randint(60,int(scrnheight - 60))
        #定义球在x,y上的移动速度，速度随机给定
        #模拟运动，不断的擦掉原来的，再在一个新的地方从新绘制
        self.xvelocity=random.randint(3,7)
        self.yvelocity=random.randint(3,7)
        #初始化屏幕的尺寸
        self.scrnwidth=scrnwidth
        self.scrnheight=scrnheight
        #定义球的半径，半径大小随机给
        self.radius=random.randint(30,70)
        #定义球的颜色
        #lambda:通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
        #计算机中的颜色都是用三个0-255之间的数字表示
        c=lambda :random.randint(0,255)
        # #%02x%02x%02x 这个好像是固定的
        self.color='#%02x%02x%02x' %(c(),c(),c())
    #创建球的函数
    def creat_ball(self):
        #通过圆心获得矩形左上角和右下角的坐标
        #这样可以获得一个固定的球
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        #tkinter没有创建圆的函数，通过创建椭圆的方式来生成圆
        #fill表示填充颜色（必须要有，要不然球没有颜色，相当于看不见）
        #outline表示外围边框的颜色
        #create_oval是canvas中的一个绘制椭圆的方法
        self.item=self.canvas.create_oval(x1,y1,x2,y2,fill=self.color,outline=self.color)

    #创建球移动的函数
    def move_ball(self):
        #球的x,y坐标根据移动速度的变化不断更新
        self.xpos +=self.xvelocity
        self.ypos +=self.yvelocity

        #当球撞到屏幕边界后，反弹移动的算法判断
        #四个方向都要判断
        if self.xpos+self.radius>=self.scrnwidth:
            #右边界撞到之后会向相反的方向进行反弹，x方向会相反
            self.xvelocity=-self.xvelocity

        if self.xpos-self.radius<=0:
            self.xvelocity= -self.xvelocity

        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity

        if self.ypos - self.radius <= 0:
            self.yvelocity = -self.yvelocity

        #在画布上移动图画
        #canvas.move方法是canvas中的一个方法，第一个参数是要移动的物体，二三参数是x轴和y轴移动的速度(距离)
        self.canvas.move(self.item,self.xvelocity,self.yvelocity)

#定义屏保的类

class ScreenSaver():
    def __init__(self):
        #将球定义为一个列表，每种球代表一个元素
        self.balls=[]
        #每次启动程序，球的数量随机
        self.num_balls=random.randint(10,30)
        #生成root主窗口
        self.root=tkinter.Tk()
        #获取屏幕尺寸，作为窗口的尺寸
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        #取消边框，将画布充满整个屏幕，参数为正则为无边框
        self.root.overrideredirect(1)
        #调整背景透明度,第一个'-alpha'好像是固定，后边数字是透明度的%比
        self.root.attributes('-alpha',0.5)
        #点击鼠标，移动鼠标，敲击键盘时退出程序，其中前面的都是固定形式
       # self.root.bind('<Motion>', self.myquit)
       # self.root.bind('<Any-Button>', self.myquit)
        self.root.bind('<Key>', self.myquit)
        # 创建画布，包括画布的归属、尺寸和背景颜色
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height, bg="black")
        #自己理解：将画布添加到窗口中
        self.canvas.pack()
        #根据num_balls随机生成的数值，在画布上生成球
        for i in range(self.num_balls):
            # 调用RandomBall函数，自动初始化出不同大小、位置和颜色的球
            ball = RandomBall(self.canvas, scrnwidth=self.width, scrnheight=self.height)
            #调用生成球的函数
            ball.creat_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()
    #调动球运动的函数
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        #after函数是每200毫秒后启动一个函数，第二个参数作为需要启动的函数，类似于递归
        self.canvas.after(50,self.run_screen_saver)
    #定义一个停止运行的函数
    def myquit(self,event):
        self.root.destroy()
#调用函数
#if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__=="__main__":
    ScreenSaver()