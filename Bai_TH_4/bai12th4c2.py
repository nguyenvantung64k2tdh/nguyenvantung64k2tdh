print ("sinh vien:Nguyen Van Tung MSV:235752021610118")
ds = input('Nhap chuoi: ').split()
element_to_remove = input("Nhập phần tử muốn xóa: ")
if element_to_remove in ds:
    ds.remove(element_to_remove)
    print(f"Đã xóa phần tử '{element_to_remove}' khỏi danh sách.")
else:
    print(f"Phần tử '{element_to_remove}' không có trong danh sách.")
print("Danh sách sau khi xóa phần tử:", ds)
