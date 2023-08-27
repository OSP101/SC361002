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
s=min(score)
S=max(score)
sc=score.index(s)
Sc=score.index(S)
print("------------------------------------")
print('คะแนนสูงสุด :',S,'วิชา :',subject[Sc])
print('คะแนนต่ำสุด :',s,'วิชา :',subject[sc])
