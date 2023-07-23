number = int(input("ป้อนตัวเลข: "))
factorial = 1
for i in range(1, number + 1):
  factorial *= i

print("ค่าแฟกทอเรียลของ {} คือ {}".format(number, factorial))