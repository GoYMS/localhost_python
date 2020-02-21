import tkinter
baseFrame = tkinter.Tk()
def  reg():
    #从输入框中得到用户输入的内容
    name = entry.get()
    pwd = entry2.get()
    t1 = len(name)
    t2 = len(pwd)
    if name == "111" and pwd =="222":
        #将登陆成功赋给label3中的text变量
        label3["text"] = "登陆成功"
    else:
        label3["text"] = "用户名或者密码错误"
        #将用户输入的内容清除
        #两个参数是从第几个删除到第几个
        entry.delete(0,t1)
        entry2.delete(0,t2)


label = tkinter.Label(baseFrame, text="账号：")
label.grid(row=0,sticky=tkinter.W)
entry = tkinter.Entry(baseFrame)
entry.grid(row=0, column=1, sticky=tkinter.E)
label2 = tkinter.Label(baseFrame, text="密码：")
label2.grid(row=1,sticky=tkinter.W)
entry2 = tkinter.Entry(baseFrame)
entry2.grid(row=1, column=1, sticky=tkinter.E)
entry2["show"]='*'
button = tkinter.Button(baseFrame,text="登录",command=reg)
button.grid(row=2, column=2, sticky=tkinter.W)
label3 = tkinter.Label(baseFrame, text="")
label3.grid(row=3)


baseFrame.mainloop()