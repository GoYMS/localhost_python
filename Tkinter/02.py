import tkinter


base = tkinter.Tk()

#负责标题
base.wm_title("Label Test")

lb = tkinter.Label(base,text="Python Label")

#给相应组件指定布局,pack是其中的一种布局
lb.pack()

base.mainloop()