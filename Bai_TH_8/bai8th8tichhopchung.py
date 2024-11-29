import tkinter as tk
from tkinter import messagebox

# Hàm hiển thị thông tin cá nhân
def show_personal_info():
    personal_info = """
    Họ tên: Nguyễn Văn Tùng
    Ngày sinh: 03/02/2005
    MSSV: 235752021610118
    Ngành học: KTĐK&TĐH
    """
    messagebox.showinfo("Thông tin cá nhân", personal_info)

# Hàm hiển thị thông tin RadioButton đang chọn
def show_selected_option():
    selected_value = selected_var.get()
    messagebox.showinfo("Thông Báo", f"Bạn đã chọn: {selected_value}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tích Hợp Giao Diện")
root.geometry("400x200")

# Tạo Frame cho phần thông tin cá nhân
personal_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
personal_frame.pack(fill="x", padx=10, pady=10)

# Tiêu đề cho phần thông tin cá nhân
personal_title = tk.Label(personal_frame, text="Thông Tin Cá Nhân", font=("Helvetica", 12, "bold"))
personal_title.pack()

# Nút hiển thị thông tin cá nhân
personal_button = tk.Button(personal_frame, text="Hiển Thị Thông Tin", command=show_personal_info, font=("Helvetica", 10))
personal_button.pack(pady=5)

# Tạo Frame cho phần RadioButton
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

# Biến lưu giá trị RadioButton
selected_var = tk.StringVar(value="1")

# Tạo các RadioButton
radio1 = tk.Radiobutton(radio_frame, text="First", variable=selected_var, value="1", font=("Helvetica", 10))
radio1.grid(row=0, column=0, padx=5, pady=10)

radio2 = tk.Radiobutton(radio_frame, text="Second", variable=selected_var, value="2", font=("Helvetica", 10))
radio2.grid(row=0, column=1, padx=5, pady=10)

radio3 = tk.Radiobutton(radio_frame, text="Third", variable=selected_var, value="3", font=("Helvetica", 10))
radio3.grid(row=0, column=2, padx=5, pady=10)

# Nút "Click Me" ngang hàng với RadioButton
click_button = tk.Button(radio_frame, text="Click Me", command=show_selected_option, font=("Helvetica", 10))
click_button.grid(row=0, column=3, padx=10, pady=10)

# Chạy giao diện chính
root.mainloop()
