print("NguyenVanTung MSV:235752021610118")
def write_list_to_file(fname, data):
    with open(fname, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(item + '\n')
data = ["Dòng 1", "Dòng 2", "Dòng 3"]
write_list_to_file('output2.txt', data)
'''dùng write(): Lặp qua từng phần tử trong danh sách
và ghi từng phần tử vào tệp, sau đó thêm ký tự xuống
dòng (\n) để mỗi phần tử bắt đầu từ dòng mới.'''