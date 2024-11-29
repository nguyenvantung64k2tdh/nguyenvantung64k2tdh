# File: sort_module.py

def bubbleSort(nlist):
    """
    Hàm sắp xếp nổi bọt (Bubble Sort) để sắp xếp danh sách 'nlist'.
    Trả về danh sách đã được sắp xếp.
    """
    n = len(nlist)
    for i in range(n):
        swapped = False
        # Duyệt qua danh sách từ đầu đến cuối, không cần xét phần tử đã được sắp xếp ở cuối
        for j in range(0, n - i - 1):
            if nlist[j] > nlist[j + 1]:
                # Hoán đổi phần tử nếu phần tử trước lớn hơn phần tử sau
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        # Nếu không có phần tử nào bị hoán đổi, mảng đã được sắp xếp
        if not swapped:
            break
    return nlist
