from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re,sys


def find_and_send_keys(xpath, text):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.send_keys(text)

def find_and_click(xpath):
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
def find_and_get_text(xpath):
    element = driver.find_element(By.XPATH, xpath).text
    return element
def webdriver_wait(xpath):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath)))

url = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ATuJsjw7UOfPexJS2oHjXCIe5ge4D5xeX1mo1NZ1momjxfe0NzGJ3MDSTpd33Zu9GTYJYrVOqEwAeA&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S285482712%3A1709709427651026&theme=glif'

user_data_dir = r'C:\Users\Admin\Desktop\HCVIP - 3\ChromeProfile\ChromeProfile\ChromeProfile - 1'
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--start-maximized')
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
options.add_argument(f'--user-data-dir={user_data_dir}')

driver = webdriver.Chrome(options=options)
driver.get(url)

find_and_send_keys('//*[@id="identifierId"]','congminh25112002@gmail.com')
find_and_click('//*[@id="identifierNext"]/div/button')
find_and_send_keys('//*[@id="password"]/div[1]/div/div[1]/input','Minhcffc@321')





