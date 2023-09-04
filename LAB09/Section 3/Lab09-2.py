subject=[]
score=[]
num=1
while True:
    if num==6:
        break
    sub=str(input('กรอกวิชาที่ {} : '.format(num)))
    subject.append(sub)
    sco=float(input('กรอกคะแนน :'))
    score.append(sco)
    num=num+1
smin=min(score)
smax=max(score)
smin_index=score.index(smin)
smax_index=score.index(smax)
print("------------------------------------")
print('คะแนนสูงสุด :',smax,'| วิชา :',subject[smax_index])
print('คะแนนต่ำสุด :',smin,'| วิชา :',subject[smin_index])
