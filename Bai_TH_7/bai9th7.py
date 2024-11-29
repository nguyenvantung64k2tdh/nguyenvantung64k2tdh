print("Nguyen Van Tung MSV:235752021610118")
import shutil

def copy_file(tungbeng,tungden):
    shutil.copy(tungbeng, tungden)

# Gọi hàm để sao chép tệp
copy_file('tungbeng.txt', 'tungden.txt')

#Hàm shutil.copy() sao chép tệp từ vị trí nguồn sang vị trí đích.
# Đây là cách đơn giản và nhanh chóng để sao chép tệp mà không cần phải mở và đọc nội dung của tệp.
#Hàm này sao chép cả nội dung và quyền truy cập (permissions) của tệp.