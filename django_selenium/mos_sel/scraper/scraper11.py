import os
import pickle
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import django 
from selenium.webdriver import DesiredCapabilities
from mos_sel.models import Flat,PaymentsEpd
from mos_sel.credentials import login,passw
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_selenium.settings")
django.setup()

URL_LOGIN='https://login.mos.ru/sps/login/methods/password?bo=%2Fsps%2Foauth%2Fae%3Fscope%3Dprofile%2Bopenid%2Bcontacts%2Busr_grps%26response_type%3Dcode%26redirect_uri%3Dhttps%3A%2F%2Fwww.mos.ru%2Fapi%2Facs%2Fv1%2Flogin%2Fsatisfy%26client_id%3Dmos.ru'
#GET_USLUGA_URL='https://www.mos.ru/services/pokazaniya-vodi-i-tepla/new/'
CAT_USLUGI='https://www.mos.ru/uslugi/'
GET_EPD='https://www.mos.ru/pgu/ru/app/guis/062301/#step_1/'
GET_USLUGA_URL='https://www.mos.ru/pgu/ru/app/guis/062301/#step_1/'
login=login
password=passw
options=Options()
#prefs={"download.default_directory":r"C:\Users\osk88\Documents\Bill_pdf","download.prompt_for_download": False,"download.directory_upgrade": True}
#prefs={"download.default_directory":"C:\\Users\\osk88\\Desktop\\Django_projects\\django_selenium\\Bill_pdf" +date.today().strftime(r"\%d\%m\%Y")+r"\\","download.prompt_for_download": False,"download.directory_upgrade": True,"plugins.always_open_pdf_externally": True}
prefs={"download.default_directory":"C:\\Users\\osk88\\Desktop\\Django_projects\\django_selenium\\Bill_pdf\\Bill_pdf","download.prompt_for_download": False,"download.directory_upgrade": True,"plugins.always_open_pdf_externally": True}
options.add_experimental_option("detach", True)
options.add_experimental_option("prefs",prefs)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
service=ChromeService(ChromeDriverManager().install())
capabilities=DesiredCapabilities.CHROME.copy()
capabilities['pageLoadStrategy']="eager"
drv = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)    

def log(url,login,password):
    
    #drv = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)    
    print("HELLO")
    #drv.delete_all_cookies()
    wait=WebDriverWait(drv,5)
    #drv.maximize_window()
    drv.set_page_load_timeout(5)
    drv.get(url)
    #drv.execute_script("window.open('{url}')".format(url=url))
    wait.until(EC.visibility_of_element_located((By.ID,"login"))).send_keys(login)
    wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
    wait.until(EC.element_to_be_clickable((By.ID,"bind"))).click()
    #print(drv.get_cookies())
    #pickle.dump(drv.get_cookies(),open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","wb"))
    return drv
    #get_cookies(drv)
    #auth
    #dr=drv
    #auth(dr)
    #auth(url)


def choose_service(url_usluga):
    """ cookies=pickle.load(open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","rb"))
    for cookie in cookies:
        drv.add_cookie(cookie)
        time.sleep(2)
    drv.refresh() """
    drv.get(url_usluga)
    return drv

def get_epd(url_epd):
    drv.get(url_epd)
    return drv

def form_fill(url_pars,name_flat):
    #drv = webdriver.Chrome(service=service,options=options,desired_capabilities=capabilities)    
    #drv=driver()
    wait=WebDriverWait(drv,5)
    drv.get(url_pars)
    #driver.execute_script("window.open('{url_pars}');".format(url_pars=url_pars))
    #time.sleep(3)
    """ cookies=pickle.load(open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","rb"))
    for cookie in cookies:
        drv.add_cookie(cookie)
        time.sleep(2)
    drv.refresh()
    time.sleep(2) """
    #print("мы здесь")
    """ try:
        wait.until(EC.presence_of_element_located((By.ID,"epd_field")),message="Элемент не найден").click()
    except TimeoutException:
        print("В настоящий момент услуга недоступна") """
    #codplat=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"home_right"))).text
    #print(codplat)
    #time.sleep(4)
    if name_flat=="ВОЙКОВСКАЯ":
        try:
            wait.until(EC.presence_of_element_located((By.ID,"epd_field")),message="Элемент не найден").click()
        except TimeoutException:
            print("В настоящий момент услуга недоступна") 
        flat_voyk=wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]//following::span[1]'.format(name_flat=name_flat))))
        codplat=flat_voyk.text
        wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat)))).click()
    else:
            try:
                wait.until(EC.presence_of_element_located((By.ID,"epd_field")),message="Элемент не найден").click()
            except TimeoutException:
                print("В настоящий момент услуга недоступна") 
            flat_kuzm=wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]//following::span[1]'.format(name_flat=name_flat.capitalize()))))
            codplat=flat_kuzm.text
            wait.until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"{name_flat}")]'.format(name_flat=name_flat.capitalize())))).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"js-find-btn"))).click()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"js-more-btn"))).click()
    """ try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME,"btn-close-pop"))).click()
    except TimeoutException:
        return False """
    return [drv,codplat,name_flat]



def parsing(data):
    #print(data)
    #cod_platelshika
    #period_oplaty
    #summa
    #data[0].switch_to.default_content()
    #print(data[0].switch_to.default_content())
    wait=WebDriverWait(data[0],5)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"js-more-btn"))).click()
    time.sleep(2)
    table_block=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"regular-blocks")))
    epd_empty=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"regular-blocks-info-paid"))).is_displayed()
    #bill_displayed=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"js-get-pdf-btn"))).is_displayed()
    bill_displayed=(table_block.find_elements(By.CLASS_NAME,'js-get-pdf-btn'))
    #epd_empty=wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"regular-blocks-info-paid"))).is_enabled()
    #epd_empty_true=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"info__right"))).text
    #epd_empty_true=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"regular-blocks-info-paid"))).find_element(By.CLASS_NAME,"info__right").text
    epd_empty_true=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"regular-blocks-info-paid"))).find_element(By.CLASS_NAME,"info__right").text
    #print(epd_empty_true)
    #print(table_block.get_attribute('innerHTML'))
    codplat=data[1]
    #codplat=data.find_element(By.CLASS_NAME,"home_right").text
    pars_data=[]
    
    
    """ assert len(data[0].window_handles) == 1 """
    
    """ if epd_empty:
        print(epd_empty)
        pars_data.append(
            {   
                'name_flat':data[2].capitalize(),
                'cod_platelshika':codplat,
                'period_oplaty':"----",
                'epd_empty':epd_empty_true,
            }
        )
        return pars_data """
    links_pdf=[]
    for y in bill_displayed:

        if y.is_displayed():
            print(y.is_displayed())
            
            y.click()
            #wait.until(EC.number_of_windows_to_be(2))
            time.sleep(2)

            header=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"popup-header")))
            link=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.component.Popup.Popup_view_pdf_box > div.popup-footer.pdf_link_block > div > div > a.pdf_link.btn")))
            links_pdf.append(link.get_attribute("href"))
            #print(link.get_attribute("href"))
            #print(header.text)
            link.click()
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.component.Popup.Popup_view_pdf_box > div.popup-header > button"))).click()
            time.sleep(1)
            """ print(data[0].window_handles)
            for window_handle in data[0].window_handles:
                if window_handle != main_page:
                    print(data[0].switch_to.window(window_handle))
                    data[0].switch_to.window(window_handle)
                    break
            time.sleep(2)
            width = data[0].get_window_size().get("width")
            height = data[0].get_window_size().get("height")
            print(width,height) """
            #drv.switch_to.frame()
            #pop_up_window=wait.until(EC.frame_to_be_available_and_switch_to_it(0))
            """ pop_up_window=data[0].find_element(By.CSS_SELECTOR,".popup-body > iframe")
            #print(pop_up_window)
            iframe=data[0].switch_to.frame(pop_up_window)
            time.sleep(5)
            print(iframe)
            pop_up_window1=data[0].find_element(By.CSS_SELECTOR,".popup-body > iframe")
            print(pop_up_window1) """
            #link=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"pdf_link.btn")))
            
            #drv.find_element(By.CLASS_NAME,"close-popup-btn").click()
            #link=wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main-content"]/a')))
            #time.sleep(3)
            #link.click()
            #data[0].switch_to.default_content()
            #print(pars_data)
    if epd_empty:
        print(epd_empty)
        pars_data.append(
            {   
                'name_flat':data[2].capitalize(),
                'cod_platelshika':codplat,
                'period_oplaty':"----",
                'epd_empty':epd_empty_true,
                'bill_save_pdf':'----'
            }
        )
        return pars_data
    else:
        pars_data.append(
                {
                'name_flat':data[2].capitalize(),
                'cod_platelshika':codplat,
                'period_oplaty': [x.text for x in table_block.find_elements(By.CLASS_NAME,"custom-control-label")],
                'summa': [x.text for x in table_block.find_elements(By.CLASS_NAME,"price") if x.text!=""],
                'bill_save_pdf':links_pdf
                
                }
                )
            #print(pars_data)
        return pars_data    
    

def save_data(data,flats):
    for item in data:
        if not 'epd_empty' in item:
            count=0
            while len(item['period_oplaty'])!=0 and len(item['summa'])!=0 and len(item['bill_save_pdf'])!=0:
            #print(item)
                try:
                    PaymentsEpd.objects.create(
                        flats_id=flats,
                        name_flat=item['name_flat'],
                        cod_platelshika=item['cod_platelshika'] ,
                        period_oplaty=item['period_oplaty'][count],
                        summa=item['summa'][count],
                        bill_save_pdf=item['bill_save_pdf'][count]
                    )
                    count+=1
                except Exception as e:
                    print('failed at latest_article is none')
                    print(e)
                    break
        else:
            for item in data:
                try:
                    PaymentsEpd.objects.create(
                    flats_id=flats,
                    name_flat=item['name_flat'],
                    cod_platelshika=item['cod_platelshika'] ,
                    period_oplaty=item['period_oplaty'],
                    summa=item['epd_empty'],
                    bill_save_pdf=item['bill_save_pdf']
                        )
                    
                except Exception as e:
                    print('failed at latest_article is none')
                    print(e)
                    break
        return print('finished')  




