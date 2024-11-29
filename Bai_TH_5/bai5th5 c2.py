print("NguyenVanTung MSV:235752021610118")
import list_utils

def main():
    # Nhập số lượng phần tử của danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))

    # Nhập giá trị các phần tử trong danh sách
    numbers = []
    for i in range(n):
        value = float(input(f"Nhập giá trị cho phần tử thứ {i + 1}: "))
        numbers.append(value)

    # Sắp xếp danh sách
    sorted_numbers = list_utils.sort_list(numbers)
    print("Danh sách sau khi sắp xếp:", sorted_numbers)

    # Tìm phần tử lớn nhất và nhỏ nhất
    max_value = list_utils.find_max(numbers)
    min_value = list_utils.find_min(numbers)
    print("Phần tử lớn nhất:", max_value)
    print("Phần tử nhỏ nhất:", min_value)


# Gọi hàm main
if __name__ == "__main__":
    main()

