from tkinter import *
app = Tk()
app.title('CALCULATOR')
app.geometry('500x500')
result = Variable(app)
value = Variable(app)
box = Entry(app, textvariable=value, width=76, bg='white',).place(x=20, y=10, height=80)

input_num = ''
def operate(e):
    global input_num
    input_num += str(e)
    value.set(input_num)

def clear():
    global input_num
    input_num = ''
    value.set('')

def output(a):
    global input_num
    value.set(eval(input_num))
    input = ''

Button(app, text='1', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('1')).place(x=20, y=190)
Button(app, text='2', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('2')).place(x=140, y=190)
Button(app, text='3', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('3')).place(x=260, y=190)
Button(app, text='4', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('4')).place(x=20, y=270)
Button(app, text='5', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('5')).place(x=140, y=270)
Button(app, text='6', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('6')).place(x=260, y=270)
Button(app, text='7', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('7')).place(x=20, y=350)
Button(app, text='8', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('8')).place(x=140, y=350)
Button(app, text='9', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('9')).place(x=260, y=350)
Button(app, text='0', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('0')).place(x=140, y=430)
Button(app, text='+', bd=2, fg='white', bg='grey',relief='raised', width=15, height=5, command=lambda:operate('+')).place(x=380, y=190)
Button(app, text='-', bd=2, fg='white', bg='grey',relief='raised', width=15, height=5, command=lambda:operate('-')).place(x=380, y=270)
Button(app, text='x', bd=2, fg='white', bg='grey',relief='raised', width=15, height=5, command=lambda:operate('*')).place(x=380, y=350)
Button(app, text='÷', bd=2, fg='white', bg='grey',relief='raised', width=15, height=5, command=lambda:operate('/')).place(x=380, y=430)
Button(app, text='=', bd=2, fg='white', bg='grey',relief='raised', width=15, height=5, command=lambda:output('=')).place(x=260, y=430)
Button(app, text='c', bd=2, fg='black', bg='orange',relief='raised', width=15, height=5, command=lambda:clear()).place(x=380, y=110)
Button(app, text='.', bd=2, fg='black', bg='white',relief='raised', width=15, height=5, command=lambda:operate('.')).place(x=20, y=430)
app.mainloop()
