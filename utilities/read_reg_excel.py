from xlrd import *

wb = open_workbook("test_data/reg_data.xlsx")
sheet = wb.sheet_by_name("Sheet1")

l=[]
def get_data():
    for i in range(2,6):
        if i==3:
            continue
        rows = sheet.row_values(i)
        testcase=rows[0]
        fname=rows[1]
        lname=rows[2]
        email=rows[3]
        pwd=rows[4]
        cpwd=rows[5]
        l.append((testcase,fname,lname,email,pwd,cpwd))
    return l







###################################################################
# reading only second row

def second_row():
    row=sheet.row_values(1)
    testcase=row[0]
    fname=row[1]
    lname=row[2]
    email=row[3]
    pwd=row[4]
    cpwd=row[5]
    return testcase,fname,lname,email,pwd,cpwd







#

def last_row():
    row=sheet.row_values(6)
    testcase=row[0]
    fname=row[1]
    lname=row[2]
    email=row[3]
    pwd=row[4]
    cpwd=row[5]
    return testcase,fname,lname,email,pwd,cpwd






# reading kavita's row
def wrong_email_format():
    row=sheet.row_values(3)
    testcase = row[0]
    fname = row[1]
    lname = row[2]
    email = row[3]
    pwd = row[4]
    cpwd = row[5]
    return testcase, fname, lname, email, pwd, cpwd




def saqib_row():
    row = sheet.row_values(7)
    testcase = row[0]
    fname = row[1]
    lname = row[2]
    email = row[3]
    pwd = row[4]
    cpwd = row[5]
    return testcase, fname, lname, email, pwd, cpwd






def saqib_last_row():
    row = sheet.row_values(8)
    testcase = row[0]
    fname = row[1]
    lname = row[2]
    email = row[3]
    pwd = row[4]
    cpwd = row[5]
    return testcase, fname, lname, email, pwd, cpwd








'''
def add():
    a = 10
    b = 20
    c = 30
    return a,b,c

x = add()
print(x)
'''







#
# def add():
#     a = 10
#     b = 20
#     c = 30
#     return a,b,c
#
# x,y,z = add()
# print(z)
#






# a,b,c,d= 'pavitra','neha','saqib','keerthana'





#######################################################################################################################

