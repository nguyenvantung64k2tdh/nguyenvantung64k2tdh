print("NguyenVanTung MSV:235752021610118")
def copy_file(tungden, tungbeng):
    with open(tungden, 'r', encoding='utf-8') as src_file:
        content = src_file.read()  # Đọc toàn bộ nội dung của tệp nguồn
    with open(tungbeng, 'w', encoding='utf-8') as dest_file:
        dest_file.write(content)  # Ghi nội dung vào tệp đích

# Gọi hàm để sao chép nội dung từ 'tungden.txt' vào 'tungbeng.txt'
copy_file('tungden.txt', 'tungbeng.txt')