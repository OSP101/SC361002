number_cha = ""
while True:
    cha = input("ป้อนอักขระ : ")
    for data in cha:
        if(data.isdigit()):
            number_cha = number_cha + data + ", "
    if(len(number_cha) != 0):
        print("------------------------------")
        print("อักขระที่ป้อนเข้ามามีตัวเลขดังนี้ :",number_cha[:-2])
        number_cha = ""
    else:
        print("------------------------------")
        print("อักขระที่ป้อนเข้ามาไม่มีตัวเลข")