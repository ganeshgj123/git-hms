from xlrd import open_workbook




def read_headers(sheet_name,test_case_name):
    book = open_workbook(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\HMSProject\data\test_data.xls")
    sheet = book.sheet_by_name(sheet_name)
    used_rows = sheet.nrows
    for i in range(0,used_rows):
        row = sheet.row_values(i)
        clean_row = [j.strip() for j in row if j.strip()]
        if clean_row:
            for item in clean_row:
                if test_case_name == item:
                    headers = sheet.row_values(i-1)
                    return ",".join([header.strip() for header in headers if header.strip()][2:])

# print(read_headers("smoke","test_registration"))
# print(read_headers("smoke","test_login_positive"))




def read_data(sheet_name,test_case_name):
    book = open_workbook(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\HMSProject\data\test_data.xls")
    wb = book.sheet_by_name(sheet_name)
    used_rows = wb.nrows
    record = []
    for i in range(1,used_rows):
        row = wb.row_values(i)
        clean_row = [j.strip() for j in row if j.strip()]
        if clean_row:
            for item in clean_row:
                if test_case_name == item and clean_row[1].upper() == "YES":
                    record.append(tuple(clean_row[2:]))
    return record

#print(read_data("smoke","test_login_positive"))











#
# def factorial(n):
#
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1)


def factorial(n):
    if n==1 or n==0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
