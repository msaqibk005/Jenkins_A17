class Welcome_page:
    reg_link = "xpath","//a[text()='Register']"
    log_link="xpath","//a[text()='Log in']"
    shopping_cart_link="xpath","//span[text()='Shopping cart']"


    def __init__(self,driver):
        self.driver=driver

    def click_reg_link(self):
        self.driver.find_element(*Welcome_page.reg_link).click()

    def click_log_link(self):
        self.driver.find_element(*Welcome_page.log_link).click()


    def click_shopping_cart(self):
        self.driver.find_element(*Welcome_page.shopping_cart_link).click()