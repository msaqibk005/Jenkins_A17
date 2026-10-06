#Testcase1:-
# enter all the data then click register button
# expected result ----> register result page should display


from time import sleep

import pytest

from pages.welcome_page import Welcome_page
from pages.register_page import Register_page
from utilities.read_reg_excel import second_row
t,f,l,e,p,cp = second_row()




def test_valid(driver):
    email = f"test{int(time.time())}@gmail.com"
    wp=Welcome_page(driver)
    wp.click_reg_link()
    sleep(3)
    rp=Register_page(driver)
    rp.click_female_gender()
    rp.enter_fname(f)
    rp.enter_lname(l)
    rp.enter_email(email)
    rp.enter_pwd(p)
    rp.enter_cpwd(cp)
    rp.click_reg_btn()
    sleep(3)

    assert driver.current_url=='https://demowebshop.tricentis.com/registerresult/1',driver.save_screenshot(f"screenshots/{t}.png")

















# Testcase2:
# # enter all the data except fname and lname then click register button
# expected result ---> same page should display (reg page)
#
# def test_invalid_flname(driver):
#     wp=Welcome_page(driver)
#     wp.click_reg_link()
#     sleep(3)
#     rp=Register_page(driver)
#     rp.click_female_gender()
#     rp.enter_fname("     ")
#     rp.enter_lname("    ")
#     rp.enter_email("kdgds@gmail.com")
#     rp.enter_pwd("1234567")
#     rp.enter_cpwd("1234567")
#     rp.click_reg_btn()
#     sleep(3)
#
#     assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot("screenshots/invalid_flname_.png")
#
#
#
#
#
#
#
#
#
# # Testcase3:
# # # enter all the data and particularly for email enter wrong format
# # then click register button
# # expected result ---> same page should display (reg page)
#
#
# def test_wrong_email_format(driver):
#     wp=Welcome_page(driver)
#     wp.click_reg_link()
#     sleep(3)
#     rp=Register_page(driver)
#     rp.click_female_gender()
#     rp.enter_fname("dschdcvvc")
#     rp.enter_lname("jhwdcvhwdvc")
#     rp.enter_email("kdgds.com")
#     rp.enter_pwd("1234567")
#     rp.enter_cpwd("1234567")
#     rp.click_reg_btn()
#     sleep(3)
#
#     assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot("screenshots/wrong_em_format.png")



from utilities.read_reg_excel import wrong_email_format
tc,fn,ln,em,pwd,cpwd = wrong_email_format()




def test_invalid_email(driver):
    wp=Welcome_page(driver)
    wp.click_reg_link()
    sleep(3)
    rp=Register_page(driver)
    rp.click_female_gender()
    rp.enter_fname(fn)
    rp.enter_lname(ln)
    rp.enter_email(em)
    rp.enter_pwd(pwd)
    rp.enter_cpwd(cpwd)
    rp.click_reg_btn()
    sleep(3)



    assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot("screenshots/email_format.png")










#
# # Testcase4:
# # # enter all the data and particularly for password enter only 4 digit password
# # then click register button
# # expected result ---> same page should display (reg page)
#
#
#
# def test_4digt_pwd(driver):
#     wp=Welcome_page(driver)
#     wp.click_reg_link()
#     sleep(3)
#     rp=Register_page(driver)
#     rp.click_female_gender()
#     rp.enter_fname("dschdcyfdqvvc")
#     rp.enter_lname("jhwdcvhwwdfdvc")
#     rp.enter_email("kdgds@gmail.com")
#     rp.enter_pwd("1234")
#     rp.enter_cpwd("1234")
#     rp.click_reg_btn()
#     sleep(3)
#
#     assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot("screenshots/4_digit_pwd.png")
#
#
#
#
#
#
#
# # Testcase5:
# # # enter all the data and keep last name field empty
# # then click register button
# # expected result ---> same page should display (reg page)
#
#
#
#
#
#
# def test_empty_lname(driver):
#     wp=Welcome_page(driver)
#     wp.click_reg_link()
#     sleep(3)
#     rp=Register_page(driver)
#     rp.click_female_gender()
#     rp.enter_fname("dscihguhdcyfdqvvc")
#     rp.enter_lname("      ")
#     rp.enter_email("kdgds@gmail.com")
#     rp.enter_pwd("123456")
#     rp.enter_cpwd("123456")
#     rp.click_reg_btn()
#     sleep(3)
#
#     assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot("screenshots/4_digit_pwd.png")
#
#
#













from utilities.read_reg_excel import get_data
import time




@pytest.mark.parametrize('t,fn,ln,em,pd,cpd',get_data())
def test_invalid_flname(t,fn,ln,em,pd,cpd,driver):
    email = f"test{int(time.time())}@gmail.com"
    wp=Welcome_page(driver)
    wp.click_reg_link()
    sleep(3)
    rp=Register_page(driver)
    rp.click_female_gender()
    rp.enter_fname(fn)
    rp.enter_lname(ln)
    rp.enter_email(email)
    rp.enter_pwd(int(pd))
    rp.enter_cpwd(int(cpd))
    rp.click_reg_btn()
    sleep(3)

    assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot(f"screenshots/{t}.png")








