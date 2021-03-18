from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()

def xz():
    cl = askcolor(title='请选择颜色')
    print(cl)

lb = Label(root,text = '')
lb.pack()
btn = Button(root,text="弹出选择文件对话框",command=xz)
btn.pack()
root.mainloop()




