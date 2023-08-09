# กำหนดค่าเริ่มต้นสำหรับค่าที่มีค่าน้อยสุดและมากสุด
minimum_value = float('inf')
maximum_value = float('-inf')
sum_values = 0
count = 0

while True:
    user_input = float(input("ป้อนตัวเลข (หากต้องการหยุดใส่ 0): "))

    if user_input == 0:
        break

    # คำนวณค่าเลขที่มีค่าน้อยสุด
    if user_input < minimum_value:
        minimum_value = user_input

    # คำนวณค่าเลขที่มีค่ามากสุด
    if user_input > maximum_value:
        maximum_value = user_input

    # นับจำนวนครั้งที่ป้อนค่า
    count += 1

    # บวกค่าเพื่อนำไปคำนวณเฉลี่ย
    sum_values += user_input

# คำนวณค่าเฉลี่ย
average = sum_values / count

print("------------------------------------------")
print("ค่าเลขที่มีค่าน้อยสุด:", minimum_value)
print("ค่าเลขที่มีค่ามากสุด:", maximum_value)
print("ค่าเฉลี่ยของตัวเลข:", average)
