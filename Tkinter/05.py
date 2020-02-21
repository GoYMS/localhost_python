import tkinter

base = tkinter.Tk()

btn1 = tkinter.Button(base,text="A")
btn1.pack(side=tkinter.TOP,expand=tkinter.YES,fill=tkinter.BOTH)
btn1 = tkinter.Button(base,text="B")
btn1.pack(side=tkinter.RIGHT,expand=tkinter.YES,fill=tkinter.NONE,anchor=tkinter.NE)
btn1 = tkinter.Button(base,text="C")
btn1.pack(side=tkinter.LEFT,expand=tkinter.NO,fill=tkinter.Y)
btn1 = tkinter.Button(base,text="D")
btn1.pack(side=tkinter.TOP,expand=tkinter.NO,fill=tkinter.BOTH)
btn1 = tkinter.Button(base,text="E")
btn1.pack(side=tkinter.BOTTOM,expand=tkinter.YES)

base.mainloop()
