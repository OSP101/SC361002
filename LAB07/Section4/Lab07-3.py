total_cost = 0

while True:
    item = int(input("ป้อนรายการสินค้า (1=เลย์, 2=โค้ก, 3=ซันซุ, 4=7-UP, 0=หยุด): "))

    if item == 0:
        break
    elif item == 1:
        total_cost += 20
    elif item == 2:
        total_cost += 42
    elif item == 3:
        total_cost += 25
    elif item == 4:
        total_cost += 19
    else:
        print("รายการสินค้าไม่ถูกต้อง")

print("ค่าสินค้าทั้งหมด:", total_cost, "บาท")
