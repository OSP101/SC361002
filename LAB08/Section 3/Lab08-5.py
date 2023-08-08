stdid = input("ป้อนรหัสนักศึกษา(ไม่ใส่ขีด) : ")
before = stdid[:-1]
after = stdid[-1]
combined = before + "-" + after
print("------------------------------")
print("รหัสนักศึกษามีขีด คือ : ",combined)