import os

# Đường dẫn đến thư mục chứa các tệp cần đổi tên
duong_dan = '/duong/dan/'

# Định dạng tên mới cho các tệp
ten_moi = 'ten_moi_{}.txt'  # Tên mới với index {}

# Lấy danh sách các tệp trong thư mục
danh_sach_tep = os.listdir(duong_dan)

# Biến đếm để tạo index cho tên mới
index = 1

# Duyệt qua từng tệp và đổi tên
for tep in danh_sach_tep:
    duong_dan_cu = os.path.join(duong_dan, tep)
    ten_tep_moi = ten_moi.format(index)  # Tạo tên mới với index tương ứng
    duong_dan_moi = os.path.join(duong_dan, ten_tep_moi)
    os.rename(duong_dan_cu, duong_dan_moi)
    index += 1
