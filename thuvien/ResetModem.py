import subprocess
import time
import socket
import requests
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

reset_modem()