import tkinter
baseFrame = tkinter.Tk()
canvas = tkinter.Canvas(baseFrame, width=700,height=300)
canvas.pack()
canvas.create_line(12,12,190,190)
canvas.create_text(120,120,text="这是一个画布你信吗？")

baseFrame.mainloop()