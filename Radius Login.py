from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="D:\Selenium Projects\Drivers\chromedriver_win32\chromedriver.exe")     #this is to invoke the chrome browser to run the script
driver.get("https://www.radiusagent.com/")  # getting the url
time.sleep(1)
driver.find_element_by_xpath("//a[normalize-space()='Log In']").click()  #finding the login button and clicking it
time.sleep(2)
un=driver.find_element_by_xpath("//input[@placeholder='Email']")    # finding the email textbox
#print("Username",un.is_displayed())     #verifying the availability of email text box
pwd=driver.find_element_by_xpath("//input[@placeholder='Password']")    #finding the password textbox
#print("Password",pwd.is_displayed())    # verifying the availability of password textbox
un.send_keys("test_radius@yopmail.com")     #sending the email to login to system
pwd.send_keys("Test@123")                    #sending the password to login to system
driver.find_element_by_xpath("//button[normalize-space()='Login']").click()
print(driver.title)
time.sleep(3)
driver.close()