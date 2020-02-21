import  tkinter

base = tkinter.Tk()

#创建一个函数来表示文本显示内容
def  showLabel():
    label = tkinter.Label(base, text="Python Label")
    label.pack()

#command 表示点击按钮后执行哪个函数
button = tkinter.Button(base, text="show label"  ,command=showLabel)
button.pack()

base.mainloop()