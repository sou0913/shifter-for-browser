# -*- coding: utf8 -*-
import sys
import tkinter as tk
import itertools
import numpy as np      
import random
import shift

root = tk.Tk()
root.title("Shifter")
root.geometry("400x700")

staticY = tk.Label(text='年')
staticY.pack()
formY = tk.Entry()
formY.pack()

staticM = tk.Label(text='月')
staticM.pack()
formM = tk.Entry()
formM.pack()

static2 = tk.Label(text='人数')
static2.pack()
form2 = tk.Entry()
form2.pack()

static3 = tk.Label(text='公休数')
static3.pack()
form3 = tk.Entry()
form3.pack()

static4 = tk.Label(text='一日の最低人数')
static4.pack()
form4 = tk.Entry()
form4.pack()

staticAH = tk.Label(text="休日の最低人数")
staticAH.pack()
formAH = tk.Entry()
formAH.pack()

static5 = tk.Label(text="最大連勤数")
static5.pack()
form5 = tk.Entry()
form5.pack()

notice = tk.Entry()

button = tk.Button(
    text='make a shift',
    command=lambda: shift.makeShift2(
                    int(formY.get()),
                    int(formM.get()),
                    int(form2.get()),
                    int(form3.get()),
                    int(form4.get()),
                    int(formAH.get()),
                    int(form5.get()),
                    notice))
button.pack(pady=20)

static6 = tk.Label(text="お知らせ")
static6.pack()
notice.pack()

root.mainloop()