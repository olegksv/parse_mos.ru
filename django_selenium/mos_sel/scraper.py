import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import django 
#from .credentials import login, passw
from selenium.webdriver import DesiredCapabilities

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_selenium.settings")
django.setup()
from mos_sel.models import Flat

URL_LOGIN='https://login.mos.ru/sps/login/methods/password?bo=%2Fsps%2Foauth%2Fae%3Fscope%3Dprofile%2Bopenid%2Bcontacts%2Busr_grps%26response_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fwww.mos.ru%2Fapi%2Facs%2Fv1%2Flogin%2Fsatisfy%26client_id%3Dmos.ru'
GET_USLUGA_URL='https://www.mos.ru/pgu/ru/app/guis/062301/#step_1'
KOD_PLAT_INPUT='//*[@id="epd_field"]'
BUUTON_FIND='//*[@id="data"]/div[1]/div[1]/div[3]/div/div[1]/a'
BUTTON_SHOW_MORE='//*[@id="step_2"]/fieldset/div[2]/div[3]/button'
LOGIN_INPUT='//*[@id="login"]'
INPUT='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
PASSWORD_INPUT='//*[@id="password"]'
BUTTON_SUBMIT='//*[@id="bind"]'
""" LOGIN=login
PASSWORD=password """


options=Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--headless")
service = Service(executable_path=(r"C:\Users\osk88\Desktop\Django_projects\django_selenium\mos_sel\chromedriver.exe"))
capabilities=DesiredCapabilities.CHROME.copy()
capabilities['pageLoadStrategy']="eager"
    

    


def log(url,login,password):
    driver = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)
    wait=WebDriverWait(driver,2)
    driver.maximize_window()
    driver.set_page_load_timeout(2)
    try:
        driver.get(url)
        wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
        wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
        #driver.find_element(By.ID,"login").send_keys(login)
        #driver.find_element(By.ID,"password").send_keys(password)
        #driver.find_element(By.ID,'bind').click()

    finally:
        return wait
    

def form_fill(url_pars,driver,name_flat):
    cookies=driver.get_cookies()
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
        time.sleep(3)
    driver.get(url_pars)
    time.sleep(4)
    driver.find_element(By.ID,"epd_field").click()
    time.sleep(4)
    codplat=driver.find_element(By.CLASS_NAME,"home_right").text
    
    # Здесь нужно Вместо ВОЙКОВСКАЯ создать переменную, которая будет выбираться
    #  в форме в django и передаваться в качестве переменной вместо "ВОЙКОВСКАЯ"
    time.sleep(4)
    if name_flat=="ВОЙКОВСКАЯ":
        driver.find_element(By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat)).click()
    else:
        driver.find_element(By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat.capitalize())).click()
    time.sleep(4)
    driver.find_element(By.CLASS_NAME,"js-find-btn").click()
    time.sleep(4)
    driver.find_element(By.CLASS_NAME,"js-more-btn").click()
    time.sleep(4)
    try:
        driver.find_element(By.CLASS_NAME,"btn-close-pop").click()
    except NoSuchElementException:
        return False
    return [driver,codplat]
    
    

def parsing(data):
    #cod_platelshika
    #period_oplaty
    #summa
    table_block=data[0].find_element(By.CLASS_NAME,"regular-blocks")
    codplat=data[1]
    #codplat=data.find_element(By.CLASS_NAME,"home_right").text
    pars_data=[]
    
    pars_data.append(
            {
            'cod_platelshika':[codplat],
            'period_oplaty': [x.text for x in table_block.find_elements(By.CLASS_NAME,"custom-control-label")],
            'summa': [x.text for x in table_block.find_elements(By.CLASS_NAME,"price")],
            }
            )
    return pars_data
    

def save_data(data):
    for item in data:
        try:
            Flat.objects.create(
               cod_platelshika=item['cod_platelshika'] ,
               period_oplaty=item['period_oplaty'],
               summa=item['summa']
            )
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')    


def main():

    auth=log(URL_LOGIN)
    fill_form=form_fill(GET_USLUGA_URL,auth)
    parse_data=parsing(fill_form)
    return save_data(parse_data)



""" def logout(driver):
    driver.find_element(By.ID,"mos-dropdown-user")
    driver.find_element(By.CLASS_NAME,) """




#options=webdriver.ChromeOptions()
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
#options.add_argument("--disable-blink-features=AutomationControlled")
#service = Service(executable_path=(r"C:\Users\osk88\Desktop\Django_projects\django_selenium\mos_sel\chromedriver.exe"))
#capabilities=DesiredCapabilities.CHROME.copy()
#capabilities['pageLoadStrategy']='eager'

""" def log(url,login,password):
    driver = webdriver.Chrome(service=service,options=options)
    wait=WebDriverWait(driver,2)
    driver.maximize_window()
    #driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    #time.sleep(5)
    #wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
    #wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
    #wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
        wait.find_element(By.ID,"login").send_keys(login)
        wait.find_element(By.ID,"password").send_keys(password)
        wait.find_element(By.ID,'bind').click()
    finally:
        return wait """

""" def log(url,login,password):
    driver = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)
    wait=WebDriverWait(driver,2)
    driver.maximize_window()
    driver.set_page_load_timeout(2)
    try:
        driver.get(url)
    
        #time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
        wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
        #driver.find_element(By.ID,"login").send_keys(login)
        #driver.find_element(By.ID,"password").send_keys(password)
        #driver.find_element(By.ID,'bind').click()
    finally:
        
        return wait 
"""

""" def log(url,login,password):
    driver = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)
    #wait=WebDriverWait(driver,2)
    driver.maximize_window()
    #driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    
        #time.sleep(5)
        #wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
        #wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
        driver.find_element(By.ID,"login").send_keys(login)
        driver.find_element(By.ID,"password").send_keys(password)
        driver.find_element(By.ID,'bind').click()
    finally:
        
        return driver 
"""