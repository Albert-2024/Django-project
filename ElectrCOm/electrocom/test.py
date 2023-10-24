from datetime import datetime
from django.forms import Select
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):   
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)

        Register = driver.find_element(By.CSS_SELECTOR, "a#cust_login")
        Register.click()
        time.sleep(2)
        
        # Register_btn = driver.find_element(By.CSS_SELECTOR, "#register-button")
        # Register_btn.click()
        # time.sleep(2)

        # user_fname = driver.find_element(By.CSS_SELECTOR, "input#first_name")
        # user_fname.send_keys("Ramanan")
        # user_lname = driver.find_element(By.CSS_SELECTOR, "input#last_name")
        # user_lname.send_keys("K M ")
        # email = driver.find_element(By.CSS_SELECTOR, "input#email")
        # email.send_keys("ramanan234@gmail.com")
        # password = driver.find_element(By.CSS_SELECTOR, "input#password")
        # password.send_keys("Ramn@123")
        # cpassword = driver.find_element(By.CSS_SELECTOR, "input#confirmPassword")
        # cpassword.send_keys("Ramn@123")
        
        
        # submitreg = driver.find_element(By.CSS_SELECTOR, "button#reg_btn")
        # submitreg.click()
        # time.sleep(2)

        username = driver.find_element(By.CSS_SELECTOR, "input#typeEmailX-2")
        username.send_keys("ramanan234@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "input#typePasswordX-2")
        password.send_keys("Ramn@123")
        time.sleep(1)
        submitc = driver.find_element(By.CSS_SELECTOR, "button#submit")
        submitc.click()
        time.sleep(2)
        
        
        product = driver.find_element(By.CSS_SELECTOR, "a#products")
        product.click()
        time.sleep(2)
        
        moreproduct = driver.find_element(By.CSS_SELECTOR, "button#more")
        driver.execute_script("window.scrollBy(0, 500);")
        moreproduct.click()
        print("Test Done")
        time.sleep(2)
        
        
#         submitc = driver.find_element(By.CSS_SELECTOR, "#addart")
#         submitc.click()
#         time.sleep(2)

#         submitc = driver.find_element(By.CSS_SELECTOR, "button#uploadButton")
#         submitc.click()
#         time.sleep(2)

#         name = driver.find_element(By.CSS_SELECTOR, "input#uploadArtist_name")
#         name.send_keys("girl setting in bed")
#         type_select = driver.find_element(By.CSS_SELECTOR, "select#uploadArt_type")
#         type_option = type_select.find_elements(By.TAG_NAME, 'option')[1]  # Assuming the first option is a placeholder
#         type_option.click()
#         size_select = driver.find_element(By.CSS_SELECTOR, "select#uploadArt_size")
#         size_option = size_select.find_elements(By.TAG_NAME, 'option')[1]  # Assuming the first option is a placeholder
#         size_option.click()
#         price = driver.find_element(By.CSS_SELECTOR, "input#uploadArt_price")
#         price.send_keys("20,000")
#         year = driver.find_element(By.CSS_SELECTOR, "input#uploadArt_year")
#         year.send_keys("2023")
#         img = driver.find_element(By.CSS_SELECTOR, "input#uploadArt_image")
#         img.send_keys(r"C:\Users\admin\OneDrive\Pictures\art1.png")
#         cer = driver.find_element(By.CSS_SELECTOR, "input#uploadArt_certificate")
#         cer.send_keys(r"C:\Users\admin\Downloads\42.pdf")
#         des = driver.find_element(By.CSS_SELECTOR, "textarea#uploadArt_summary")
#         des.send_keys("Women setting in bed reading a letter")

#         submitart = driver.find_element(By.CSS_SELECTOR, "button#upload-art-submit")
#         submitart.click()
#         time.sleep(2)
# submitc = driver.find_element(By.CSS_SELECTOR, "#viewart")
#         submitc.click()
#         time.sleep(2)
#         driver.execute_script("window.scrollBy(0, 500);")
#         time.sleep(2)

#         submitc = driver.find_element(By.CSS_SELECTOR, "#lgout")
#         submitc.click()
#         time.sleep(2)


#         username = driver.find_element(By.CSS_SELECTOR, "input#user_email")
#         username.send_keys("admin1")
#         password = driver.find_element(By.CSS_SELECTOR, "input#user_password")
#         password.send_keys("admin123")
#         time.sleep(1)
#         submitc = driver.find_element(By.CSS_SELECTOR, "button#submit")
#         submitc.click()
#         time.sleep(2)

#         submitc = driver.find_element(By.CSS_SELECTOR, "#artapprove")
#         submitc.click()
#         time.sleep(2)

#         driver.execute_script("window.scrollBy(-500, 0);")
#         time.sleep(2)

#         submitc = driver.find_element(By.XPATH, "//button[contains(text(),'Approve')]")
#         submitc.click()
#         time.sleep(2)

#         submitc = driver.find_element(By.CSS_SELECTOR, "#lgout")
#         submitc.click()
#         time.sleep(2)




#         username = driver.find_element(By.CSS_SELECTOR, "input#user_email")
#         username.send_keys("tony")
#         password = driver.find_element(By.CSS_SELECTOR, "input#user_password")
#         password.send_keys("Tony@123")
#         time.sleep(1)
#         submitc = driver.find_element(By.CSS_SELECTOR, "button#submit")
#         submitc.click()
#         time.sleep(2)

#         submitc = driver.find_element(By.CSS_SELECTOR, "#art")
#         submitc.click()
#         time.sleep(2)

#         driver.execute_script("window.scrollBy(0, 600);")
#         time.sleep(2)

#         print("Test Done")
        
        


# if name == 'main':
#     import unittest
#     unittest.main()