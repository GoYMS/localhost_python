import pygame
from pygame.locals import *

def start():
    #创建一个窗口，用来充当背景
    screen=pygame.display.set_mode((480,890),0,32)
    #创建一个和窗口大小一样的图片，用来当背景
    image_file_path='./image/background.jpg'
    background=pygame.image.load(image_file_path).convert()
    #创建一个飞机对象
    hero_plane=HeroPlane(screen)
    #把背景图片放到窗口中显示
    while True:
        screen.blit(background,(0,0))
        hero_plane.display()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key==K_a or event.key == K_LEFT:
                    hero_plane.move_left()
                elif event.key==K_d or event.key == K_RIGHT:
                    hero_plane.move_right()
                elif event.key == K_SPACE:
                    hero_plane.launch_bullet()
        pygame.display.update()




#显示玩家飞机，控制移动方向
class HeroPlane(object):
    def __init__(self,screen):
        #设置飞机的默认位置
        self.x=230
        self.y=600
        #设置要显示内容的窗口
        self.screen=screen
        #用来保存英雄飞机需要的图片名字
        self.image_name="./image/hero.png"
        #根据名字生成飞机图片
        self.image=pygame.image.load(self.image_name).convert()
        # 用来存储飞机发射的子弹
        self.bullet_list = []
    #在默认位置显示玩家飞机
    def display(self):
        #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))
        #用来存储放需要删除的对象的信息
        need_del_list=[]
        #保存需要删除的对象
        for item in self.bullet_list:
            if item.judge():
                need_del_list.append(item)
        #删除需要删除的对象
        for del_item in need_del_list:
            self.bullet_list.remove(del_item)
        for bullet in  self.bullet_list:
            bullet.display()
            bullet.move()
    #让飞机左移动
    def move_left(self):
        self.x -=10
    # 让飞机右移动
    def move_right(self):
        self.x +=10
    def launch_bullet(self):
        new_bullet = Bullet(self.x,self.y,self.screen)
        self.bullet_list.append(new_bullet)


#玩家飞机发射子弹
class Bullet(object):
    def __init__(self,x,y,screen):
        self.x= x+40
        self.y= y-20
        self.screen= screen
        self.image=pygame.image.load("./image/bullet-3.png").convert()
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y -= 2
    def judge(self):
        if self.y < 0 :
            return True
        else:
            return False

if __name__=='__main__':
    start()