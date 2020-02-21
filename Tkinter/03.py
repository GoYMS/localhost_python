import  tkinter


base = tkinter.Tk()
base.wm_title("Lable lest")
#支持的属性有很多，例如，background ,font ,underline等
#第一个参数，指定所属
lbl  = tkinter.Label(base, text="Python Lable")
lbl.pack()
lb2  = tkinter.Label(base, text="绿色背景",  background="green")
lb2.pack()
lb3  = tkinter.Label(base, text="红色背景",  background="red")
lb3.pack()

base.mainloop()
