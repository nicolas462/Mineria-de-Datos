import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__absolutepath__ = os.path.abspath(__file__)
__fileDirectory__ = os.path.dirname(__absolutepath__)
__exePath__ = os.path.join(__fileDirectory__, 'assets', 'geckodriver.exe')
__credentialsPath__ = os.path.join(__fileDirectory__, 'assets', 'credentials.txt')
__inputPath__ = os.path.join(__fileDirectory__, 'assets', 'input.txt')

def login(email, password):
    try:
        global driver
        try:
            driver = webdriver.Firefox(executable_path=__exePath__)
            driver.get('https://facebook.com/')
            driver.maximize_window()
            print('Web driver has initialized.')
        except:
            print('Web driver error.')
            exit()

        # filling the form
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('pass').send_keys(password)
        time.sleep(3)
        # clicking on login button
        driver.find_element_by_name('login').click()
    except:
        print('Something went wrong.')

def main():
    with open(__credentialsPath__) as f:
        email = f.readline().split('"')[1]
        password = f.readline().split('"')[1]

        if email == "" or password == "":
            print("Your email or password is missing. Kindly write them in credentials.txt")
            exit()

    ids = ["https://facebook.com/" + line.split("/")[-1] for line in open(__inputPath__, newline='\n')]

    if len(ids) > 0:
        print("\nStarting Scraping...")
        login(email, password)
        time.sleep(5)
        print(ids)      
        driver.get(ids[0])
        driver.close()
    else:
        print("Input file is empty.")    

if __name__ == '__main__':
    main()