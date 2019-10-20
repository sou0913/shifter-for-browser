w_or_h_1d = [0,0,0,0,0,1,1]
>>> m_1d = [3,4,2,4,5,3,4]
>>> y = [w_or_h_1d, m_1d]







import itertools
import numpy as np
import random
import openpyxl
import pprint
import tkinter as tk
import calendar
import datetime

wb = openpyxl.load_workbook('/Users/so/Desktop/book.xlsx')

sheet = wb['Sheet1']

empty = [""] * 31
empty_2d = []
for i in range(10):
    empty_2d.append(empty)

def makeDates(year, month):
    date_1d = []
    days = calendar.monthrange(year, month)[1]
    for day in range(1, days+1):
        date_1d.append(datetime.date(year, month, day))
    return [1 if i.weekday() >= 5 else 0 for i in date_1d]

def write_list_2d(sheet, l_2d, start_row, start_col):
    for y, row in enumerate(l_2d):
      for x, cell in enumerate(row):
          sheet.cell(row=start_row + y,
                     column=start_col + x,
                     value=cell)

def makeShift2(year, month, members, holidays, atLeast, atHoliday, continuous, notice):
    days = calendar.monthrange(year, month)[1]
    for k in range(100):
        s_2d = []
        for j in range(members):
            for i in range(100):
                h_d1 = random.sample(range(days), k=holidays)
                one = [1] * days
                for h in h_d1:
                    one[h] = 0
                one_st = "".join(str(n) for n in one)
                renkin = [1] * (continuous + 1)
                renkin_st = "".join(str(n) for n in renkin)
                if i == 99:
                    notice.delete(0, tk.END)
                    notice.insert(tk.END, "連勤数に修正が必要です")
                    return
                elif renkin_st in one_st:
                    continue
                else:
                    break
            s_2d.append(one)
        m_1d = np.sum(s_2d, axis=0)
        w_or_h_1d = makeDates(year, month)
        y = [w_or_h_1d, m_1d]
        m_h_1d = [y[1][i] for i, cell in enumerate(m_1d) if y[0][i]==1] 
        if k == 99:
            notice.delete(0, tk.END)
            notice.insert(tk.END, "見つかりませんでした")
        elif np.all(m_1d >= atLeast) and np.all(m_h_1d >= atHoliday):
            s2_2d = []
            for s_1d in s_2d:
                s2_1d = ["" if i == 1 else "○" for i in s_1d]
                s2_2d.append(s2_1d)
            write_list_2d(sheet, empty_2d, 2, 2)
            write_list_2d(sheet, s2_2d, 2, 2)
            wb.save('/Users/so/Desktop/book.xlsx')
            notice.delete(0, tk.END)
            notice.insert(tk.END, "作成しました!")
            break
        else:
            continue


