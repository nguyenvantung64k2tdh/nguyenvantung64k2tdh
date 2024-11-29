print("Nguyen Van Tung MSV:235752021610118")
import datetime as dt

# Định nghĩa định dạng ngày giờ
format = '%Y-%m-%dT%H:%M:%S'

# Phân tích chuỗi ngày giờ cụ thể thành một đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# Truy xuất và in ra các phần cụ thể của ngày giờ
print('Ngày ' + str(t1.day))
print('Tháng ' + str(t1.month))
print('Phút ' + str(t1.minute))
print('Giây ' + str(t1.second))

# Định nghĩa ngày và giờ hiện tại
t2 = dt.datetime.now()

# Tính toán sự khác biệt về ngày giữa ngày hiện tại và ngày cụ thể
diff = t2 - t1
print('Chênh lệch bao nhiêu ngày? ' + str(diff.days))
