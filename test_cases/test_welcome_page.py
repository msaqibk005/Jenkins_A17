#testcase1:-
# 1. launch browser
# 2. click on reg link
# 3. verify register page displayed or not


from pages.welcome_page import Welcome_page
from time import sleep
import pytest


def test_click_reglink(driver):
    Wc = Welcome_page(driver)
    Wc.click_reg_link()
    sleep(3)

    assert driver.current_url=='https://demowebshop.tricentis.com/register',driver.save_screenshot("screenshots/reglink.png")




#testcase2:-
# 1. launch browser
# 2. click on login link
# 3. verify login page displayed or not





def test_click_loglink(driver):
    Wc = Welcome_page(driver)
    Wc.click_log_link()
    sleep(4)

    assert driver.current_url=='https://demowebshop.tricentis.com/login',driver.save_screenshot("screenshots/loglink.png")











#testcase3:-
# 1. launch browser
# 2. click on shopping cart link
# 3. verify cart page displayed or not








#testcase4:-
# 1. launch browser
# 2. click on wishlist
# 3. verify wishlist page displayed or not






#testcase5:-
# 1. launch browser
# 2. verify register link is displayed or not