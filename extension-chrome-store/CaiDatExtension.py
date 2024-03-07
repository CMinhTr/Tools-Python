from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui

from selenium.webdriver.support import expected_conditions as EC
# AddExtension = r'C:\Users\Admin\Desktop\HCVIP - 3\AddExtension.png'
# image_clicker = ImageClicker()
# for i in range(1,6):
# user_data_dir = f'C:\\Users\\Admin\\Desktop\\HCVIP - 3\\ChromeProfile\\ChromeProfile\\ChromeProfile - {i}'
options = webdriver.ChromeOptions()
# options.add_argument(f'--user-data-dir={user_data_dir}')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
start_time = time.time()
time_wait = 10
print(start_time)
# while time.time() < start_time + time:

#try:
driver.get("https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn")
add_click = driver.find_element(By.XPATH,'//span[text()="Add to Chrome" or text()="Thêm vào Chrome"]')
add_click.click()

time.sleep(5)
pyautogui.press('tab')
pyautogui.press('space')

#WebDriverWait(driver,timeout=300).until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Xóa khỏi Chrome or text()="Remove from Chrome"]')))
WebDriverWait(driver,timeout=300).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div/div/div/ul/li[1]/div/h2')))


print('Cài đặt thành công')
driver.quit()