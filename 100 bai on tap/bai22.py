diem_toan = float(input("Nhập điểm toán: "))
diem_van = float(input("Nhập điểm văn: "))
diem_anh = float(input("Nhập điểm Anh: "))
if 0 <= diem_toan <= 10 and 0 <= diem_van <= 10 and 0 <= diem_anh <= 10:
    diem_trung_binh = (diem_toan + diem_van + diem_anh) / 3
    if diem_trung_binh >= 8 and diem_toan >= 8 and diem_van >= 8 and diem_anh >= 6.5:
        print("Học sinh giỏi")
    elif diem_trung_binh >= 6.5 and diem_toan >= 6.5 and diem_van >= 6.5 and diem_anh >= 5:
        print("Học sinh khá")
    elif diem_trung_binh >= 5 and diem_toan >= 5 and diem_van >= 5 and diem_anh >= 3.5:
        print("Học sinh trung bình")
    elif diem_trung_binh >= 3.5 and diem_toan >= 3.5 and diem_van >= 3.5 and diem_anh >= 2:
        print("Học sinh yếu")
    else:
        print("Học sinh kém")
else:
    print("Điểm không hợp lệ. Vui lòng nhập điểm trong khoảng từ 0 đến 10.")