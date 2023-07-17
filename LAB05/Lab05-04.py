score = float(input("กรุณาป้อนเกรดเฉลี่ย: "))
d_grade = input("เคยได้เกรด D มาก่อนหน้านี้หรือไม่? (ใช่/ไม่): ")
if score >= 3.25:
    grade = "ระดับคะแนนเฉลี่ย: ดีมาก"
elif score >= 2.75:
    grade = "ระดับคะแนนเฉลี่ย: ดี"
elif score >= 2.00:
    grade = "ระดับคะแนนเฉลี่ย: พอใช้"
else:
    grade = "ระดับคะแนนเฉลี่ย: ต้องปรับปรุง"

if d_grade == "ใช่":
    honor = "คุณไม่ได้รับเกียรตินิยม"
else:
    honor = "คุณได้รับเกียรตินิยม"

print("ระดับเกรดเฉลี่ย: {}".format(grade))
print(honor)