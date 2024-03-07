import cv2, pyautogui
import numpy as np
import win32com.client
import subprocess, requests, socket, time

class ExcelApp:
    def __init__(self):
        excel_app = win32com.client.GetActiveObject("Excel.Application")
        excel_app.Visible = True
        self.workbook = excel_app.ActiveWorkbook
        self.sheet = self.workbook.ActiveSheet

    def read_excel(self, _range):
        return self.sheet.Range(_range).Value

    def write_excel(self, _range, _value):
        self.sheet.Range(_range).Value = _value
        self.save_excel()

    def save_excel(self):
        self.workbook.Save()

class ImageClicker:
    def __init__(self):
        pass

    @staticmethod
    def find_image_location(template_path, threshold=0.8):
        # Đọc ảnh màn hình
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Đọc ảnh template
        template = cv2.imread(template_path)

        # Tìm kiếm vị trí của template trong ảnh màn hình
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            return max_loc
        else:
            return None

    @staticmethod
    def click_on_image(template_path):
        # Đọc ảnh template
        template = cv2.imread(template_path)

        location = ImageClicker.find_image_location(template_path)

        if location is not None:
            # Lấy tọa độ trung tâm của template
            center_x = location[0] + template.shape[1] // 2
            center_y = location[1] + template.shape[0] // 2

            # Thực hiện click chuột tại tọa độ trung tâm
            pyautogui.click(center_x, center_y)
            print("Đã click vào hình ảnh.")
        else:
            print("Không tìm thấy hình ảnh trên màn hình.")

# Example Usage:
# excel = ExcelApp()
# image_clicker = ImageClicker()

# # Đường dẫn đến file template ảnh cần click
# template_path = r'C:\Users\Admin\Desktop\HCVIP - 3\DeleteChrome.png'

# # Thực hiện click chuột
# image_clicker.click_on_image(template_path)

# # Đọc giá trị từ Excel và hiển thị
# data_from_excel = excel.read_excel("A1:B2")
# print("Dữ liệu từ Excel:", data_from_excel)


def reset_modem():
    network_name = "Mobifone"

   
    subprocess.run(["rasdial", network_name, "/disconnect"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(f"! Ngắt Kết Nối - {time.strftime('%H:%M:%S')}")
    subprocess.run(["rasdial", network_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print(f"! Kết Nối - {time.strftime('%H:%M:%S')}")

    def ping(host, timeout):
        try:
            socket.create_connection((host, 80), timeout)
            return True
        except OSError:
            return False
    

    def get_external_ip():
        try:
            # Sử dụng API của httpbin.org để lấy thông tin IP
            response = requests.get('https://httpbin.org/ip')
            data = response.json()
            
            # Trích xuất địa chỉ IP từ dữ liệu JSON
            ip_address = data['origin']
            
            return ip_address
        except Exception as e:
            print(f"Lỗi khi lấy địa chỉ IP: {e}")
            return None
    start_time = time.time()
    while time.time() - start_time < 5:
        if ping('google.com', 1):
            print("! Có Mạng")
            time.sleep(1)
            # In ra địa chỉ IP ngoại tuyến
            external_ip = get_external_ip()
            if external_ip:
                print(f"! Địa chỉ IP hiện tại: {external_ip}")
            return 1
        time.sleep(1)
    
    print("Không Có Mạng, Thử Lại")
    return reset_modem()

# Thử chạy hàm reset_modem
#reset_modem()