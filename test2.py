import subprocess
import socket
import time

class ModemResetter:
    def __init__(self, network_name="Mobifone"):
        self.network_name = network_name

    def execute_rasdial(self, command):
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    def log_message(self, message):
        print(f"! {message} - {time.strftime('%H:%M:%S')}")

    def ping(self, host, timeout):
        try:
            socket.create_connection((host, 80), timeout)
            return True
        except OSError:
            return False

    def reset_modem(self):
        self.log_message("Ngắt Kết Nối")
        self.execute_rasdial(["rasdial", self.network_name, "/disconnect"])
        time.sleep(0.199)

        self.log_message("Kết Nối")
        self.execute_rasdial(["rasdial", self.network_name])

        start_time = time.time()
        while time.time() - start_time < 5:
            if self.ping('google.com', 1):
                self.log_message("Có Mạng")
                time.sleep(1)
                return 1
            time.sleep(1)

        self.log_message("Không Có Mạng, Thử Lại")
        return self.reset_modem()

# Sử dụng class ModemResetter
modem_resetter = ModemResetter()
result = modem_resetter.reset_modem()
print(f"Result: {result}")
