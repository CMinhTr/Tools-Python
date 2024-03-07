from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time,re,sys
sys.path.insert(0,r'C:\Users\Admin\Desktop\HCVIP - 3\Tools Py')
from thuvien.thuvien import *

ExcelApp = ExcelApp()
CoKetQua = 'C'


for i in range (1,6):
    ExcelApp.save_excel()
    if ExcelApp.read_excel(f'{CoKetQua}{i}') != None:
        continue
    
    DD_ProfileChrome = ExcelApp.read_excel(f'A{i}')
    if DD_ProfileChrome == None: sys.exit('Next DD_ProfileChrome Not Found!!!')
    print(f'{i} - DD_ProfileChrome: {DD_ProfileChrome}')
    
    Email = ExcelApp.read_excel(f'F{i}')
    if Email == None: sys.exit('Next Email Not Found!!!')
    print(f'{i} - Email: {Email}')

    PassWord = ExcelApp.read_excel(f'G{i}')
    if Email == None: sys.exit('Next PassWord Not Found!!!')
    print(f'{i} - PassWord: {PassWord}')

    EmailRecovery = ExcelApp.read_excel(f'H{i}')
    if EmailRecovery == None: sys.exit('Next EmailRecovery Not Found!!!')
    print(f'{i} - EmailRecovery: {EmailRecovery}')

    # options = uc.ChromeOptions()
    # options.add_argument("--ignore-certificate-error")
    # options.add_argument("--ignore-ssl-errors")
    # options.add_argument("--profile-directory={TenProfile}")
    # options.add_argument(f'--user-data-dir={DD_ProfileChrome}')
    # # Khởi tạo trình duyệt với các tùy chọn đã thiết lập
    # driver = uc.Chrome(options=options)

    # driver.get('https://accounts.google.com/')
    # # add email
    # driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(email)
    # driver.find_element(By.XPATH, '//*[@id="identisfierNext"]/div/button/span').click()
    # time.sleep(10)
    # driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    # driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    # time.sleep(10)
    # driver.quit()
    
    