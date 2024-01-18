chuoi = input("Nhập vào một chuỗi: ")
chuoi = ''.join(e for e in chuoi if e.isalnum() or e.isspace())
tu=chuoi.split()
if len(tu) > 0:
    tu_dau_tien = tu[0]
    print("Từ đầu tiên trong chuỗi:", tu_dau_tien)
else:
    print("Chuỗi không có từ.")