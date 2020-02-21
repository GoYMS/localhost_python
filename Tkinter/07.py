import tkinter

baseFrame = tkinter.Tk()
#这种消息机制的函数必有至少有一个参数，并且第一个参数必须是event
def baseLabel(event):
          label = tkinter.Label(baseFrame, text="谢谢点击")
          label.pack()

label_2 = tkinter.Label(baseFrame, text="模拟按钮")
#label_2绑定相应的消息和处理函数
label_2.bind("<Button-1>",baseLabel)
label_2.pack()

baseFrame.mainloop()