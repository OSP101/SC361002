stdid = input("ป้อนรหัสนักศึกษา : ")
index_stdid = stdid.find("-")
before = int(stdid[index_stdid-1])
after = int(stdid[index_stdid+1])
summation = before + after
print("------------------------------")
print("รหัสนักศึกษาที่ป้อนเข้ามา คือ : ",stdid)
print("เลขหน้าขีด คือ : ",before)
print("เลขหลังขีด คือ : ",after)
print("ผลรวม : ",summation)