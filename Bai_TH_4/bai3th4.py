print ("Sinh vien:Nguyen Van Tung MSV:235752021610118")
S = input('Nhap chuoi:')
for ch in S:
    if ch not in [' ','\t']:
        print(ch.upper())
