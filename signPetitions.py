from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from links import *

links = get_links()

rFName = input("Enter first name: ")
rLName = input("Enter last name: ")
rEmail = input("Enter email:")

def signPetition(link):
        driver = wd.Chrome(ChromeDriverManager().install())
        driver.get(link)
        first = driver.find_element_by_name("firstName")
        last = driver.find_element_by_name("lastName")
        email = driver.find_element_by_name("email")
        display = driver.find_element_by_name("public")
        sign = driver.find_element_by_xpath("""//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]""")
        first.send_keys(rFName)
        last.send_keys(rLName)
        email.send_keys(rEmail)
        display.click()
        sign.click()
        print("success")
        driver.delete_all_cookies()
        driver.quit()

errors = []

for i in range(len(links)):
    try:
        signPetition(links[i])
    except:
        errors.append(links[i])
        print("There was an error with this link. All unsigned links will be printed at the end.")

print("The following petitions were not signed, you can manually sign them:")
for e in errors:
    print(e)
