import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import django 
from selenium.webdriver import DesiredCapabilities
from mos_sel.models import Flat
from mos_sel.credentials import login,passw
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_selenium.settings")
django.setup()



URL_LOGIN='https://login.mos.ru/sps/login/methods/password?bo=%2Fsps%2Foauth%2Fae%3Fscope%3Dprofile%2Bopenid%2Bcontacts%2Busr_grps%26response_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fwww.mos.ru%2Fapi%2Facs%2Fv1%2Flogin%2Fsatisfy%26client_id%3Dmos.ru'
GET_USLUGA_URL='https://www.mos.ru/pgu/ru/app/guis/062301/#step_1'
KOD_PLAT_INPUT='//*[@id="epd_field"]'
BUUTON_FIND='//*[@id="data"]/div[1]/div[1]/div[3]/div/div[1]/a'
BUTTON_SHOW_MORE='//*[@id="step_2"]/fieldset/div[2]/div[3]/button'
LOGIN_INPUT='//*[@id="login"]'
INPUT='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
PASSWORD_INPUT='//*[@id="password"]'
BUTTON_SUBMIT='//*[@id="bind"]'
login=login
password=passw

def browser():
    options=Options()
    #options.add_experimental_option("detach", True)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument("--headless")
    service = Service(executable_path=(r"C:\Users\osk88\Desktop\Django_projects\django_selenium\mos_sel\chromedriver.exe"))
    capabilities=DesiredCapabilities.CHROME.copy()
    capabilities['pageLoadStrategy']="eager"
    driver = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)    
    return driver
    


def log(url,drv,login,password):
    wait=WebDriverWait(drv,2)
    drv.maximize_window()
    drv.set_page_load_timeout(2)
    drv.get(url)
    wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
    return drv

def form_fill(url_pars,driver,name_flat):
    wait=WebDriverWait(driver,5)
    cookies=driver.get_cookies()
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
        driver.refresh()
    #time.sleep(4)
    driver.set_page_load_timeout(2)
    driver.get(url_pars)
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID,"epd_field"))).click()
    #time.sleep(4)
    #driver.find_element(By.ID,"epd_field").click()
    #time.sleep(4)
    #codplat=driver.find_element(By.CLASS_NAME,"home_right").text
    codplat=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"home_right"))).text
    time.sleep(4)
    if name_flat=="ВОЙКОВСКАЯ":
        #driver.find_element(By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat)).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat)))).click()
    else:
        #driver.find_element(By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat.capitalize())).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat.capitalize())))).click()
    #time.sleep(4)
    #driver.find_element(By.CLASS_NAME,"js-find-btn").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"js-find-btn"))).click()
    #time.sleep(4)
    #driver.find_element(By.CLASS_NAME,"js-more-btn").click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"js-more-btn"))).click()
    #time.sleep(4)
    try:
        #driver.find_element(By.CLASS_NAME,"btn-close-pop").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn-close-po"))).click()
    except TimeoutException:
        return False
    """     except NoSuchElementException:
        return False """
    return [wait,codplat]


def main():

    brw=browser()
    auth=log(URL_LOGIN,brw,login,password)
    fill_form=form_fill(GET_USLUGA_URL,auth,"Кузьминки")






