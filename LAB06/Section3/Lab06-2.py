number = input("กรุณาป้อนตัวเลขทีี่ต้องการรวม: ")
sum = 0
while (number != "No"):
  sum += int(number)
  number = input("กรุณาป้อนตัวเลขทีี่ต้องการรวม: ")
print("ผลลัพธ์รวมทั้งสิ้น", sum)