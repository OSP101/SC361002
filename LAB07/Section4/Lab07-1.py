minimum_value = float('inf')
maximum_value = float('-inf')
sum_values = 0
count = 0

user_input = float(input("ป้อนตัวเลข (หากต้องการหยุดใส่ 0): "))

while user_input != 0:
    if user_input < minimum_value:
        minimum_value = user_input

    if user_input > maximum_value:
        maximum_value = user_input

    count += 1
    sum_values += user_input

    user_input = float(input("ป้อนตัวเลข (หากต้องการหยุดใส่ 0): "))

if count == 0:
    print("ไม่มีข้อมูลตัวเลข")
else:
    average = sum_values / count
    print("------------------------------------------")
    print("ค่าเลขที่มีค่าน้อยสุด:", minimum_value)
    print("ค่าเลขที่มีค่ามากสุด:", maximum_value)
    print("ค่าเฉลี่ยของตัวเลข:", average)

