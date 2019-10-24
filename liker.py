#bot that I created to like all my friend's pictures!

#DEPENDENCIES (See ReadMe)
#selenium,geckodriver,python3.XX,current instagram account

#import the libraries
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# uname = input('please input your instagram username')
# pword = input('please input your corressponding password')
#
#
# def usrnme(username):
# #a little username validation for ya (phone number, username, or email)
#     while (len(username) <=0):
#         print('username cant be blank!')
#         username = input('actually enter in your instagram username this time!')
# def passwd(password):
#     while (len(password) == 0):
#         print('password cant be blank')
#         password = input('actually enter in your password this time!')
# usrnme(uname)
# passwd(pword)

#TODO: add the verification function in order to confirm the login credentials

#def verification(dsc):
#    print('currently the bot has your username as: ' , uname)
#    print('currently the bot has your password as: ',pword)
#    if dsc == 'yes' or dsc == 'y':
#        print('Awesome!, launching the bot!')
#    else:
#        x = input('r for try again --- q for Quit')
#        if x == 'r' or x == 'R':
uname = 
pword = 
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
#insta blocks you if you go to quickly
time.sleep(3)
#find all the buttons that I need to click in order to log on
usernamebox = browser.find_element_by_name('username')
time.sleep(3)

passwordbox = browser.find_element_by_name('password')


#fill in the login-information you gave the bot
usernamebox.send_keys(uname)
time.sleep(3)
passwordbox.send_keys(pword)

passwordbox.send_keys(Keys.RETURN)

time.sleep(3)
# add an if statement to click the not now to notifcations

browser.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
time.sleep(5)
# find all 'hearts' presented on the page
likes = browser.find_elements_by_xpath("//span[@class='fr66n']")
print(len(likes))
print("WORKS")
browser.maximize_window()

#initiate the for loop to like the pictures in a baby buffalo manner

for h in range(len(likes)):
    ActionChains(browser).move_to_element(likes[h]).click(likes[h]).perform()
    print(likes[h])
    time.sleep(3)
