print("sinh vien:Nguyen Van Tung MSV:235752021610118")
def fibonacci_list(n):
    fib_list = []
    a, b = 0, 1
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

# Nhập số nguyên n từ người dùng
n = int(input("Nhập số nguyên n: "))
print(f"Các số Fibonacci nhỏ hơn {n} là:")
print(fibonacci_list(n))
