from xlrd import open_workbook


#
# def read_data(sheetname):
#     data = {}
#     book = open_workbook(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\HMSProject\data\locators.xls")
#     sheet = book.sheet_by_name(sheetname)
#     used_rows = sheet.nrows
#     for row in range(1,used_rows):
#         row = sheet.row_values(row)
#         data[row[0]] = (row[1],row[2])
#     return data

# print(read_data("homepage"))



def attach_locator(sheetname):
    def read_data(cls):           #adminpage = read_data(AdminPage)
        book = open_workbook(
            r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\HMSProject\data\locators.xls")
        sheet = book.sheet_by_name(sheetname)
        used_rows = sheet.nrows
        for row in range(1, used_rows):
            row = sheet.row_values(row)
            setattr(cls,row[0],(row[1], row[2]))
        return cls
    return read_data

