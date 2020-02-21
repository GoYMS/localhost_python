import tkinter

baseFrame = tkinter.Tk()
def makeLabel():
    tkinter.Label(baseFrame, text="点击重庆火锅我就出现").pack()

menubar = tkinter.Menu(baseFrame)

for item in ['麻辣肘子','肯德基','德克士']:
    #添加分隔符
    menubar.add_separator()
    menubar.add_command(label=item)
menubar.add_command(label="重庆火锅",command=makeLabel)
def pop(event):
    #Menu类里面有一个post方法，它接收两个参数，即x和y坐标，它会在相应的位置弹出菜单。
    menubar.post(event.x_root,event.y_root)

baseFrame.bind("<Button-3>", pop)

baseFrame.mainloop()