number = int(input("ป้อนตัวเลขที่ต้องการ: "))
res = 0
for i in range(1,number+1):
    if((number%i)==0):
        res += 1
if(res == 2):
    print(number,"เป็นจำนวนเฉพาะ")
else:
    print(number,"ไม่เป็นจำนวนเฉพาะ")