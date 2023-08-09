total_credit = 0
total_grade_points = 0

while True:
    credit = int(input("ป้อนหน่วยกิต (หากต้องการหยุดใส่ 0): "))
    if credit == 0:
        break

    grade = float(input("ป้อนเกรด (ตัวเลข): "))

    total_credit += credit
    total_grade_points += credit * grade

print("------------------------------------------")
gpa = total_grade_points / total_credit
print('เกรดเฉลี่ยรวม: %.2f' %gpa)
