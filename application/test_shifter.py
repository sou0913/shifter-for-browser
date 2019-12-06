import unittest
import shifter as sf 
import openpyxl

class ShifterTest(unittest.TestCase):
    def test_get_value_list(self):
        wb_test = openpyxl.load_workbook('static/books/test.xlsx', read_only=False, keep_vba=True)
        sheet_test = wb_test['Sheet1']
        t_2d = sheet_test["A1:C3"]
        expectation = [[0],[1],[1,2]]
        self.assertEqual(expectation, sf.get_value_list(t_2d))

    def test_makeDates(self):
        year = 2019
        month = 12
        expectation = [1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0]
        self.assertEqual(expectation, sf.makeDates(year,month))
    
    def test_write_list_2d(self):
        wb_test = openpyxl.load_workbook('static/books/test.xlsx', read_only=False, keep_vba=True)
        sheet_test = wb_test['Sheet1']
        t_2d = [["○","○",""],["","","○"],["","",""]]
        # (1,1)から(3,3)までは最初のテストで使っているので。
        self.assertEqual("success!",sf.write_list_2d(sheet_test,t_2d,4,1))
    def test_makeShift2_normal(self):
        year = 2019
        month = 12
        members = 5
        holidays = 9
        atLeast = 2
        atHoliday = 3
        continuous = 5
        response = sf.makeShift2(year,month,members,holidays,atLeast,atHoliday,continuous)
        self.assertTrue(isinstance(response, int))
    def test_makeShift2_fix(self):
        year = 2019
        month = 12
        members = 5
        holidays = 9
        atLeast = 2
        atHoliday = 3
        #連勤数が異常値
        continuous = 0
        self.assertEqual("fix",sf.makeShift2(year,month,members,holidays,atLeast,atHoliday,continuous))
    def test_makeShift2_unable(self):
        # 困難または不可能な条件
        year = 2019
        month = 12
        members = 5
        holidays = 9
        atLeast = 3
        atHoliday = 5
        continuous = 5
        self.assertEqual("unable",sf.makeShift2(year,month,members,holidays,atLeast,atHoliday,continuous))

if __name__ == "__main__":
    unittest.main()