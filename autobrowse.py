#use this to open a browser window and login to a form
# to run this you are going to need the selenium library installed
# along with a current version of geckodriver
# import the libraries

import selenium
from selenium import webdriver

#set the browser type to a new firefox session (change browser with .Chrome or which ever you want)
browser = webdriver.Firefox()

#goto the site that I want
browser.get('https://mail.ship.edu/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fmail.ship.edu%2fowa')

#find the fields that I want to fill out ( username , password, submit button)
usernamebox = browser.find_element_by_name('username')
passwordbox = browser.find_element_by_name('password')
loginbutton = browser.find_element_by_class_name('signinbutton')

#Actually fill in the fields that I found in the step previous
usernamebox.send_keys('your_shipid')
passwordbox.send_keys('your_password')

#hit the login button and
loginbutton.click()
