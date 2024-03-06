import subprocess
import time
import socket

def reset_modem():
    network_name = "Mobifone"

    def execute_rasdial(command):
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    def log_message(message):
        print(f"! {message} - {time.strftime('%H:%M:%S')}")

    def ping(host, timeout):
        try:
            socket.create_connection((host, 80), timeout)
            return True
        except OSError:
            return False

    log_message("Ngắt Kết Nối")
    execute_rasdial(["rasdial", network_name, "/disconnect"])
    time.sleep(0.199)

    log_message("Kết Nối")
    execute_rasdial(["rasdial", network_name])

    start_time = time.time()
    while time.time() - start_time < 5:
        if ping('google.com', 1):
            log_message("Có Mạng")
            time.sleep(1)
            return 1
        time.sleep(1)

    log_message("Không Có Mạng, Thử Lại")
    return reset_modem()

# Thử chạy hàm reset_modem

