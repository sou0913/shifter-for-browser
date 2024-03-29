# 最初は一人づつのシフトの直積を取ろうとしてましたが、計算量が多く断念。
import itertools
import numpy as np
import random
import openpyxl
import calendar
import datetime
import time


wb = openpyxl.load_workbook('static/books/book.xlsx', read_only=False, keep_vba=True)

sheet = wb['Sheet1']

# 入力された二次元行列の空でない要素のindexを一次元で返す。
def get_value_list(t_2d):
    return([[i for i, cell in enumerate(row) if cell.value is not None] for row in t_2d])
# openpyxlにより、Excelシートの内容を二次元行列で取得。
l_2d = get_value_list(sheet["B2:AE7"])

# 初期化するための空の二次元配列を作成
empty = [""] * 31
empty_2d = []
for i in range(10):
    empty_2d.append(empty)

def makeDates(year, month):
    date_1d = []
    days = calendar.monthrange(year, month)[1] # [0]は月の初日の曜日番号
    for day in range(1, days+1):
        date_1d.append(datetime.date(year, month, day)) # datetime.dateの返り値はdateオブジェクト
    return [1 if i.weekday() >= 5 else 0 for i in date_1d]　# 土日1, 平日0の1次元リスト

# 作ったシフトをExcelのSheetに記入する。Sheetは1始まり。
def write_list_2d(sheet, t_2d, start_row, start_col):
    for y, row in enumerate(t_2d):
      for x, cell in enumerate(row):
          sheet.cell(row=start_row + y,
                     column=start_col + x,
                     value=cell)
    return "success!"

def makeShift2(year, month, members, holidays, atLeast, atHoliday, continuous):
    # 以下では1が出勤、0が休み。
    days = calendar.monthrange(year, month)[1]
    for k in range(10000):
        s_2d = []
        for j in range(members):
            for i in range(10000):
                h_d1 = random.sample(range(days), k=holidays)
                one = [1] * days
                for h in h_d1:
                    one[h] = 0
                # randomで制作した一行のシフトを文字列に変換
                one_st = "".join(str(n) for n in one)
                renkin = [1] * (continuous + 1)
                renkin_st = "".join(str(n) for n in renkin)
                # 希望休制度
                # randamで生成したシフト中の、希望休日の値を取得
                # kibou_genzitu_1d = [one[i] for i in l_2d[j]]
                if i == 9999:
                    return "fix"
                elif renkin_st in one_st:
                    continue
                # 希望休制度
                # np.anyは、一つでもtrueならtrueを返す。
                # elif kibou_genzitu_1d != [] and np.any(np.array(kibou_genzitu_1d) > 0):
                #     continue
                else:
                    break
            s_2d.append(one)
        m_1d = np.sum(s_2d, axis=0)
        w_or_h_1d = makeDates(year, month) #返り値は土日1,平日0のリスト
        y = [w_or_h_1d, m_1d]
        # 土日の人数取得
        m_h_1d = [y[1][i] for i, cell in enumerate(m_1d) if y[0][i]==1] 
        if k == 9999:
            return "unable"
        elif np.all(m_1d >= atLeast) and np.all(np.array(m_h_1d) >= atHoliday):
            s2_2d = []
            for s_1d in s_2d:
                s2_1d = ["" if i == 1 else "○" for i in s_1d]
                s2_2d.append(s2_1d)
            write_list_2d(sheet, empty_2d, 2, 2)
            write_list_2d(sheet, s2_2d, 2, 2)
            ut = time.time()
            tag = round(ut)
            wb.save(f'static/books/book{tag}.xlsx')
            return tag
        else:
            continue


