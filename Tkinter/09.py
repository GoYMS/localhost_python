import tkinter

baseFrame = tkinter.Tk()
#将菜单行放在baseFrame上
menubar = tkinter.Menu(baseFrame)

for item in ['File', 'Edit', 'View', 'About']:
    menubar.add_command(label=item)
    
#属性menu指定使用哪一个作为顶级菜单
baseFrame["menu"]=menubar
baseFrame.mainloop()
