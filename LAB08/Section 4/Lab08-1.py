cha_data = ""
while True:
    cha = input("ป้อนอักขระ : ")
    if(cha == "Y"):
        break
    cha_data += cha
print("-----------------------------------")
print("อักขระ A มีจำนวน ",cha_data.count("A")," ตัว")
print("อักขระ B มีจำนวน ",cha_data.count("B")," ตัว")
print("อักขระอื่น ๆ มีจำนวน ",len(cha_data)-(cha_data.count("A")+cha_data.count("B"))," ตัว")