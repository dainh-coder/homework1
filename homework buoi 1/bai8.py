ten1 = input("Ten chu ho: ")
chi_so_thang_trc1 = float(input("Chi so thang trc: "))
x1 = float(input("Chi so thang nay: "))
luong_dien = x1 - chi_so_thang_trc1
if 0 <= luong_dien <= 50:
    tien_phai_tra = (1.984 * luong_dien) * 1.08
elif 51 <= luong_dien <= 100:
    tien_phai_tra = (1.984 * 50 + 2.050 * (luong_dien - 50)) * 1.08
elif 101 <= luong_dien <= 200:
    tien_phai_tra = (1.984 * 50 + 2.050 * 50 + 2.380 * (luong_dien - 100)) * 1.08
elif 201 <= luong_dien <= 300:
    tien_phai_tra = (1.984 * 50 + 2.050 * 50 + 2.380 * 100 + 2.998 * (luong_dien - 200)) * 1.08 # Chú ý: giá bậc 4 là 2.998, code cũ của bạn ghi là 2.980
elif 301 <= luong_dien <= 400:
    tien_phai_tra = (1.984 * 50 + 2.050 * 50 + 2.380 * 100 + 2.998 * 100 + 3.350 * (luong_dien - 300)) * 1.08
elif luong_dien >= 401:
    tien_phai_tra = (1.984 * 50 + 2.050 * 50 + 2.380 * 100 + 2.998 * 100 + 3.350 * 100 + 3.460 * (luong_dien - 400)) * 1.08
print(f"Ho va ten: {ten1}")
print(f"Tien phai tra la: {tien_phai_tra:.0f}")
