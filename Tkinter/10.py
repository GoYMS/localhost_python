import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)
menubar1 = tkinter.Menu(menubar)
for item in ["Copy","Past","Cut"]:
    menubar1.add_command(label=item)
menubar.add_cascade(label="File")
#最后的menu=menubar1的意思是说将二级菜单连接到Edit下边
menubar.add_cascade(label="Edit",menu=menubar1)
menubar.add_cascade(label="About")
baseFrame["menu"] = menubar

baseFrame.mainloop()