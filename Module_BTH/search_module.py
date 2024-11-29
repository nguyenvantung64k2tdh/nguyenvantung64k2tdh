#search_module.py
def Sequential_Search(dlist, item):
    """
    Hàm tìm kiếm tuyến tính: Tìm phần tử 'item' trong danh sách 'dlist'.
    Trả về một tuple (found, index), trong đó:
    - found: True nếu tìm thấy, False nếu không tìm thấy.
    - index: Chỉ mục của phần tử nếu tìm thấy, hoặc -1 nếu không tìm thấy.
    """
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)  # Tìm thấy phần tử, trả về True và chỉ mục
    return (False, -1)  # Không tìm thấy phần tử, trả về False và -1
#search_module.py
def binary_search(sorted_list, value):
    """
    Hàm tìm kiếm nhị phân: Tìm phần tử 'value' trong danh sách đã được sắp xếp 'sorted_list'.
    Trả về True nếu tìm thấy, False nếu không tìm thấy.
    """
    lower_bound = 0
    upper_bound = len(sorted_list) - 1

    while lower_bound <= upper_bound:
        mid_point = lower_bound + (upper_bound - lower_bound) // 2
        if sorted_list[mid_point] == value:
            return True  # Tìm thấy phần tử
        elif sorted_list[mid_point] < value:
            lower_bound = mid_point + 1  # Tìm kiếm nửa phải
        else:
            upper_bound = mid_point - 1  # Tìm kiếm nửa trái

    return False  # Không tìm thấy phần tử
