
"""
#随机生成我们需要的名字
import tkinter
import random

baseFrame = tkinter.Tk()

def random_1():
    s1 = ['邓论','陈伟霆','鹿晗']
    s = random.choice(s1)
    return s
def random_2():
    s2 = ['杨紫','刘亦菲','杨颖']
    s = random.choice(s2)
    return s
def button_click():
    man = random_1()
    woman = random_2()
    sentence = man + "喜欢" +woman
    result.delete(0,tkinter.END)
    result.insert(0,sentence)

button = tkinter.Button(baseFrame,text="随机匹配",command=button_click)
result = tkinter.Entry(baseFrame)
result.pack()
button.pack()



baseFrame.mainloop()
"""
"""
#登录界面
import tkinter

def button_click():
    name = entry.get()
    pwd = entry1.get()
    if name == "YMS" and pwd == "123456":
        entry3["text"] = "登陆成功"
    else:
        entry3["text"] = "用户名或密码错误，请重新登录"
        entry.delete(0,tkinter.END)
        entry1.delete(0, tkinter.END)

baseFrame = tkinter.Tk()
label_1 = tkinter.Label(baseFrame, text="用户名")
label_1.grid(row=0,column=0)
entry = tkinter.Entry(baseFrame)
entry.grid(row=0,column=1)
label_2 = tkinter.Label(baseFrame, text="密码")
label_2.grid(row=1,column=0)
entry1 = tkinter.Entry(baseFrame)
entry1.grid(row=1,column=1)
entry1['show'] = '*'
button = tkinter.Button(baseFrame,text="登录",command=button_click)
button.grid(row=2,column=2)
entry3 = tkinter.Label(baseFrame,text="")
entry3.grid(row=2,column=1)

baseFrame.mainloop()
"""

