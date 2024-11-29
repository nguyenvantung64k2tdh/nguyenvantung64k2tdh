print ("sinh vien:Nguyen Van Tung MSV:235752021610118")
ds = input('Nhap chuoi: ').split()
element_to_find = input("Nhập phần tử cần tìm: ")
try:
    index = ds.index(element_to_find)
    print(f"Phần tử '{element_to_find}' nằm ở chỉ số {index}.")
except ValueError:
    print(f"Phần tử '{element_to_find}' không có trong danh sách.")
