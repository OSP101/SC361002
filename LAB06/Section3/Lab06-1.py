score = input("โปรดป้อนคะแนนของคุณ (หากต้องการหยุดให้ป้อน n): ")
while (score != "n"):
  score = int(score)
  if score >= 80:
      grade = "A"
  elif score >= 75:
      grade = "B+"
  elif score >= 70:
      grade = "B"
  elif score >= 65:
      grade = "C+"
  elif score >= 60:
      grade = "C"
  elif score >= 55:
      grade = "D+"
  elif score >= 50:
      grade = "D"
  else:
      grade = "F"
  print("เกรดของคุณคือ", grade)
  score = input("โปรดป้อนคะแนนของคุณ (หากต้องการหยุดให้ป้อน n): ")