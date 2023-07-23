start_number = int(input("ป้อนเลขเริ่มต้น: "))
end_number = int(input("ป้อนเลขสิ้นสุด: "))

odd_number_count = 0
for number in range(start_number, end_number + 1):
  if number % 2 != 0:
    odd_number_count += 1

print("จำนวนเลขคี่ที่อยู่ระหว่าง {} ถึง {} คือ {} ตัว".format(start_number, end_number, odd_number_count))
