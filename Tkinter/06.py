import tkinter
baseFrame = tkinter.Tk()

label = tkinter.Label(baseFrame, text="账号：")
label.grid(row=0,sticky=tkinter.W)
entry = tkinter.Entry(baseFrame)
entry.grid(row=0, column=1, sticky=tkinter.E)
label2 = tkinter.Label(baseFrame, text="密码：")
label2.grid(row=1,sticky=tkinter.W)
entry2 = tkinter.Entry(baseFrame)
entry2.grid(row=1, column=1, sticky=tkinter.E)
entry2['show']='*'
button = tkinter.Button(baseFrame,text="登录")
button.grid(row=2, column=1, sticky=tkinter.W)
label3 = tkinter.Label(baseFrame,text="")
label3.grid(row=3)


baseFrame.mainloop()
