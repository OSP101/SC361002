angle1 = int(input("ป้อนขนาดของมุมแรก: "))
angle2 = int(input("ป้อนขนาดของมุมที่สอง: "))
angle3 = int(input("ป้อนขนาดของมุมที่สาม: "))

total = angle1 + angle2 + angle3
if angle1 + angle2 + angle3 != 180:
  print("มุมทั้งหมดรวมกันต้องไม่เกิน 180 องศา!!")
else:
  if angle1 == angle2 == angle3:
    print("ขนาดมุมรวมทั้งหมด:",total)
    print("สามเหลี่ยมด้านเท่า")
  elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("ขนาดมุมรวมทั้งหมด:",total)
    print("สามเหลี่ยมมุมฉาก")
  elif angle1 < 90 and angle2 < 90 and angle3 < 90:
    print("ขนาดมุมรวมทั้งหมด:",total)
    print("สามเหลี่ยมหน้าจั่ว")
  else:
    print("ขนาดมุมรวมทั้งหมด:",total)
    print("สามเหลี่ยมด้านไม่เท่า")