subject = []
while True:
    print("========== ฟังก์ชันการทำงาน ==========")
    print("a : เพิ่มรายวิชา")
    print("d : ลบรายวิชา")
    print("p : พิมพ์รายวิชา")
    print("y : จบการทำงาน")
    select = input("โปรดเลือกฟังก์ชั่น : ")
    if(select == "a"):
        print("---------------------------------")
        data = input("ป้อนวิชาที่ต้องการจะเพิ่ม : ")
        subject.append(data)
    elif(select == "d"):
        print("---------------------------------")
        data = input("ป้อนวิชาที่ต้องการจะลบ : ")
        subject.remove(data)
        continue
    elif(select == "p"):
        print("---------------------------------")
        print("วิชาทั้งหมด :",subject)
    elif(select == "y"):
        print("จบการทำงาน")
        break
