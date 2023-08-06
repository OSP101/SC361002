total_tolls = 0
count = 0

while count < 5:
    vehicle_type = int(input("ป้อนประเภทของรถ (1=รถยนต์บุคคล, 2=รถตู้, 3=รถโดยสาร, 4=รถบรรทุก): "))

    if vehicle_type == 1:
        total_tolls += 40
    elif vehicle_type == 2:
        total_tolls += 60
    elif vehicle_type == 3:
        total_tolls += 80
    elif vehicle_type == 4:
        total_tolls += 100
    else:
        print("ประเภทรถไม่ถูกต้อง")
        continue

    count += 1

print("ค่าทางพิเศษรวมทั้งหมด:", total_tolls, "บาท")
