import cv2
import pyautogui
import numpy as np
import win32com.client

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
