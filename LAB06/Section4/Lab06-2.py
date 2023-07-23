sum = 0
while True:
  number = input("กรุณาป้อนตัวเลขทีี่ต้องการรวม: ")
  if number == "No":
      break
  sum += int(number)

print("ผลลัพธ์รวมทั้งสิ้น", sum)