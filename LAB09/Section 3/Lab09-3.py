A=(80,'A')
B=(70,'B')
C=(50,'F')
while True:
    scoer = float(input("กรอกคะแนน : "))
    if scoer >= A[0]:
        print('คะแนน :', scoer,"ได้เกรด :", A[1])
    elif scoer >= B[0]:
        print('คะแนน :', scoer,"ได้เกรด :", B[1])
    elif scoer < C[0]:
        print('คะแนน :', scoer,"ได้เกรด :", C[1])