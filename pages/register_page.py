class Register_page:
    gender_female="id","gender-female"
    gender_male="id","gender-male"
    fname='id',"FirstName"
    lname='id','LastName'
    email='id','Email'
    pwd='id','Password'
    cpwd='id','ConfirmPassword'
    reg_btn='id','register-button'


    def __init__(self,driver):
        self.driver=driver

    def click_female_gender(self):
        self.driver.find_element(*Register_page.gender_female).click()


    def click_male_gender(self):
        self.driver.find_element(*Register_page.gender_male).click()



    def enter_fname(self,fname):
        self.driver.find_element(*Register_page.fname).send_keys(fname)


    def enter_lname(self,lname):
        self.driver.find_element(*Register_page.lname).send_keys(lname)


    def enter_email(self,email):
        self.driver.find_element(*Register_page.email).send_keys(email)


    def enter_pwd(self,pwd):
        self.driver.find_element(*Register_page.pwd).send_keys(pwd)


    def enter_cpwd(self,cpwd):
        self.driver.find_element(*Register_page.cpwd).send_keys(cpwd)



    def click_reg_btn(self):
        self.driver.find_element(*Register_page.reg_btn).click()



