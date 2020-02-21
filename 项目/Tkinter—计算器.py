from tkinter import*
from decimal import Decimal
root=Tk()
#定义面板大小
root.geometry("300x500")
#起名字
root.title("计算器")
#定义面板
frame_show=Frame(width=300,height=150,bg='#bbbbbb')
#添加到主窗体
frame_show.pack()
#定义顶部区域
#代表字符串，能变化，具有一定的功能，显示
sv=StringVar()
sv.set('0')
#Label用于在指定的窗口中显示文本和图像。
# 最终呈现出的Label是由背景和前景叠加构成的内容。
#anchor:定义控件的锚点，e代表右边
#justify:对齐方式
show_label=Label(frame_show,textvariable=sv,\
                 bg='green',width=20,height=3,\
                 font=("黑体",20,'bold'),\
                  justify=LEFT,anchor='e')
#padx和pady的作用是填充
show_label.pack(padx=10,pady=10)

#定义按钮区域
frame_bord=Frame(width=400,height=350,bg='#cccccc')
#在使用Tkinter模块编写图像界面时，经常用到pack()和grid()进行布局管理，
# pack()参数较少，使用方便，是最简单的布局，但是当控件数量较多时，
# 可能需要使用grid()进行布局
#定义按钮所表示功能的函数
def delete():
    global num1,num2,All
    if All!='':
        #isdigit( )函数是检测输入字符串是否只由数字组成。
        if All[-1].isdight():
            if All ==num1:
                num1=num1[0:len(num1)-1]
            else:
                num2=num2[0:len(num2)-1]
        All=All[0:len(All)-1]
        sv.set(All)
def clean():
    global num1,num2,operator,All
    num1 = ''
    num2 = ''
    operator = ''
    All = ''
    sv.set('0')
def jiajian():
    global num1,num2,All,operator
    if All != '':
        if All[-1].isdigit() and num2 == '':
            if All[0] == '-':
                num1 = str(abs(float(num1)))
                All = num1
            else:
                Num1 = float(num1) * (-1)
                num1 = str(Num1)
                All = num1
        elif All[-1].isdigit() and num2 != '':
            Num2 = float(num2) * (-1)
            All = All.replace(num2, str(Num2))
            num2 = str(Num2)
        else:
            pass
        sv.set(All)
def ce():
    sv.set('0')
button_ce = Button(frame_bord, text="CE", width=9, height=2, command=ce).grid(row=0, column=0)
button_clean=Button(frame_bord,text="C",width=9,height=2,command=clean).grid(row=0,column=1)
button_delete=Button(frame_bord,text="←",width=9,height=2,command=delete).grid(row=0,column=2)
button_jiajian=Button(frame_bord,text="±",width=9,height=2,command=jiajian).grid(row=4,column=0)

num1=''
num2=''
operator=''
All=''
def change(num):
    global num1,num2,All,operator
    if operator=='=':
        if num != '.':
            operator =''
            num1=str(num)
            All=num1
            sv.set(All)
    elif operator=='':
        if num == '.'and num1=='':
            pass
        elif num=='.' and '.' in num1:
            pass
        else:
            num1=num1+str(num)
            All =All +str(num)
            sv.set(All)
    else:
        if num == '.' and num2 == '':
            pass
        elif num == '.' and '.' in num2:
            pass
        else:
            num2 = num2 + str(num)
            All = All + str(num)
            # 如果是第二个操作数，则应显示完整的计算式子
            sv.set(All)
def res(s):
	if s[0] == '-':
		for i in s[1:len(s)]:
			if i in ['+','-','*','/']:
				op = i
				li = s.split(op)
				if s.count('-') == 3:
					Al = i+'Decimal(li[1])'+i+i+'Decimal(li[3])'
				elif s.count('-') == 2 and i == '-':
					Al = i+'Decimal(li[1])'+i+'Decimal(li[2])'
				else :
					Al = 'Decimal(li[0])'+i+'Decimal(li[1])'
				return(eval(Al))
				break
	else :
		for i in s:
			if i in ['+','-','*','/']:
				op = i
				li = s.split(op)
				if s.count('-') == 2:
					Al = 'Decimal(li[0])'+i+i+'Decimal(li[2])'
				else :
					Al = 'Decimal(li[0])'+i+'Decimal(li[1])'
				return(eval(Al))
				break

def operation(op):
    global num1, num2, operator, All
    if op == '-' and num1 == '':
        All = All + op
        sv.set(op)
        print(All)
    elif num1 != '' and All[-1].isdigit() and op in ['+', '-', '×', '÷'] and num2 == '':
        operator = op
        All = All + op
        sv.set(All)
        print(All)
    elif op == '-' and All[-2].isdigit() and All[-1] in ['+', '-', '×', '÷'] and num2 == '':
        operator = op
        All = All + op
        sv.set(All)
        print(All)
    elif num2 != '' and num2[-1].isdigit() and op in ['+', '-', '×', '÷']:
        operator = op
        num1 = str(eval("res(All)"))
        All = num1 + operator
        sv.set(All)
        print(All)
        num2 = ''
    elif All != '' and op == '=' and All[-1].isdigit():
        if operator != '=':
            operator = op
            num1 = str(eval("res(All)"))
            All = num1
            sv.set(All)
            print(All)
            num2 = ''


button_chu=Button(frame_bord,text="➗",width=9,height=2,command=lambda :operation('÷')).grid(row=0,column=3)
#button_fan=Button(frame_bord,text="±",width=9,height=1,command=fan).grid(row=0,column=3)
button_7=Button(frame_bord,text=7,width=9,height=2,command=lambda:change("7")).grid(row=1,column=0)
button_8=Button(frame_bord,text=8,width=9,height=2,command=lambda:change("8")).grid(row=1,column=1)
button_9=Button(frame_bord,text=9,width=9,height=2,command=lambda:change("9")).grid(row=1,column=2)
button_cheng=Button(frame_bord,text="X",width=9,height=2,command=lambda :operation('X')).grid(row=1,column=3)
button_4=Button(frame_bord,text=4,width=9,height=2,command=lambda:change("4")).grid(row=2,column=0)
button_5=Button(frame_bord,text=5,width=9,height=2,command=lambda:change("5")).grid(row=2,column=1)
button_6=Button(frame_bord,text=6,width=9,height=2,command=lambda:change("6")).grid(row=2,column=2)
button_jian=Button(frame_bord,text="—",width=9,height=2,command=lambda :operation('-')).grid(row=2,column=3)
button_1=Button(frame_bord,text=1,width=9,height=2,command=lambda:change("1")).grid(row=3,column=0)
button_2=Button(frame_bord,text=2,width=9,height=2,command=lambda:change("2")).grid(row=3,column=1)
button_3=Button(frame_bord,text=3,width=9,height=2,command=lambda:change("3")).grid(row=3,column=2)
button_jia=Button(frame_bord,text="+",width=9,height=2,command=lambda :operation('+')).grid(row=3,column=3)

button_0=Button(frame_bord,text=0,width=9,height=2,command=lambda:change("0")).grid(row=4,column=1)
button_dian=Button(frame_bord,text=".",width=9,height=2,command=lambda :operation('.')).grid(row=4,column=2)
button_deng=Button(frame_bord,text="=",width=9,height=2,command=lambda :operation('=')).grid(row=4,column=3)
frame_bord.pack(padx=10,pady=10)
root.mainloop()