number = int(input("ป้อนตัวเลขที่ต้องการ: "))
count = 1
res = 0
while (count != (number+1)):
    print(number)
    if (number % count)==0:
        res += 1
    count += 1
if(res == 2):
    print(number,"เป็นจำนวนเฉพาะ")
else:
    print(number,"ไม่เป็นจำนวนเฉพาะ")