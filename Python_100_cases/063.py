# 题目：画椭圆。　
# 程序分析：使用 Tkinter。

# !/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from tkinter import *

    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=500, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
