from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time


def login_details(email,password,driver):

    try:
        getEmail = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        getPassword = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )

        getLogin = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-cy='login-button']"))
        )
        getEmail.send_keys(email)
        getPassword.send_keys(password)
        getLogin.click()


    except TimeoutException as ex:
        print(dir(ex))
        print(ex.message)


def login_to_new_window(driver):

    driver.get('https://app.apollo.io/#/login')

    ''' applying the demo for the apolloscraper'''
    '''
    driver.execute_script("window.open('https://app.apollo.io/#/login','new window')")
    driver.switch_to.window(driver.window_handles[1])
    '''
    login_details("bsimran18@tbc.edu.np","bu11etproof@97",driver)
    try:
        check_if_login_error = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CLASS_NAME,"zp-icon apollo-icon apollo-icon-alert-triangle zp_2BRav zp_35LDu zp_16f5V")))
        login_details("***************","*********",driver)
    except:
        print('No security issue on login')
    return driver
