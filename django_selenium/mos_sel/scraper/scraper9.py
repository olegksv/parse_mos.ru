import os
import pickle
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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_selenium.settings")
django.setup()

URL_LOGIN='https://login.mos.ru/sps/login/methods/password?bo=%2Fsps%2Foauth%2Fae%3Fscope%3Dprofile%2Bopenid%2Bcontacts%2Busr_grps%26response_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fwww.mos.ru%2Fapi%2Facs%2Fv1%2Flogin%2Fsatisfy%26client_id%3Dmos.ru'
GET_USLUGA_URL='https://www.mos.ru/services/pokazaniya-vodi-i-tepla/new/'
#GET_USLUGA_URL='https://www.mos.ru/pgu/ru/app/guis/062301/#step_1'
login=login
password=passw


def driver():
    options=Options()
    options.add_experimental_option("detach", True)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service=ChromeService(ChromeDriverManager().install())
    capabilities=DesiredCapabilities.CHROME.copy()
    capabilities['pageLoadStrategy']="eager"
    drv = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)    
    return drv

def log(url,login,password):
    print("HELLO")
    drv=driver()
    drv.delete_all_cookies()
    wait=WebDriverWait(drv,5)
    drv.maximize_window()
    drv.set_page_load_timeout(5)
    drv.get(url)
    #drv.execute_script("window.open('{url}')".format(url=url))
    wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
    #print(drv.get_cookies())
    pickle.dump(drv.get_cookies(),open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","wb"))
    return drv
    #get_cookies(drv)
    #auth
    #dr=drv
    #auth(dr)
    #auth(url)

def auth():
    drv=driver()
    drv.get(URL_LOGIN)
    drv.delete_all_cookies()
    time.sleep(2)
    print("Тут")
    cookies=pickle.load(open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","rb"))
    for cookie in cookies:
        drv.add_cookie(cookie)
        time.sleep(1)
    drv.refresh()
    return drv
    #dr.refresh()
    #return dr





def form_fill(url_pars,drv,name_flat):
    
    #drv=driver()
    wait=WebDriverWait(drv,5)
    drv.get(url_pars)
    #driver.execute_script("window.open('{url_pars}');".format(url_pars=url_pars))
    time.sleep(5)
    """ cookies=pickle.load(open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
        time.sleep(5)
    driver.refresh()
    time.sleep(2) """
    print("мы здесь")
    try:
        wait.until(EC.presence_of_element_located((By.ID,"epd_field")),message="Элемент не найден").click()
    except TimeoutException:
        print("В настоящий момент услуга недоступна")
    codplat=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"home_right"))).text
    time.sleep(4)
    if name_flat=="ВОЙКОВСКАЯ":
        wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat)))).click()
    else:
        wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat.capitalize())))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"js-find-btn"))).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"js-more-btn"))).click()
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn-close-po"))).click()
    except TimeoutException:
        return False
    return [wait,codplat]








