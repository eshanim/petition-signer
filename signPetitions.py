from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from links import *
from faker import Faker

fake = Faker()

links = get_links()

rFName = input("Enter first name: ")
rLName = input("Enter last name: ")
print("Emails have to be randomly generated to avoid Change.org account-making policies.")
driver = wd.Chrome(ChromeDriverManager().install())

def sendForm(link):
        driver.get(link)
        first = driver.find_element_by_name("firstName")
        last = driver.find_element_by_name("lastName")
        email = driver.find_element_by_name("email")
        sign = driver.find_element_by_xpath("""//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]""")
        display = driver.find_element_by_name("public")
        first.send_keys(rFName)
        last.send_keys(rLName)
        fEmail = fake.email()
        email.send_keys(fEmail)
        display.click()
        sign.click()
        print("success")
        driver.delete_all_cookies()

errors = []

for i in range(len(links)):
    try:
        sendForm(links[i])
    except:
        errors.append(links[i])
        print("There was an error with this link. All unsigned links will be printed at the end.")

print("These didn't work, you can manually sign them:")
for e in errors:
    print(e)
