#-*- coding:UTF-8 -*-
'''
Created on 2018年9月3日

@author: 007
'''
#图像界面GUI编程，tkinter库
from tkinter import *
import tkinter.simpledialog as dl#将tkinter.simpledialog简称为dl，直接操作dl即可，as可有可无
import tkinter.messagebox as mb#tkinter.messagebox简称为mb，直接操作mb即可，as可有可无

r = Tk()#创建一个变量root，Tk()是tkinter库里面的一个构造函数，创建一个主程序的显示框
w = Label(r,text = "Label Title")#创建一个标签，Label也是tkinter里面的一个函数，在主函数框root里面创建一个标签，显示文字的标题为Label Title
w.pack()#Label自带一个方法pack()自动调节窗口适应标签字数

mb.showwarning("警告", "点确定后会弹出Welcome Message")
mb.showerror("Welcome", "Welcome Message")#showerror方法，展示信息的窗口
guess = dl.askinteger("Number", "Enter a number")#askinteger提供用户输入的对话框（int型），然后赋给guess,第一个参数Number为标题，第二个为提示语
  
output = 'This is a output message'#定义一个字符串
mb.showinfo("Output", output)#showinfo方法，向用户展示信息
print(guess)#显示用户输入的整形值

