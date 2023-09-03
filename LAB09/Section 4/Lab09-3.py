A=(80,'A')
B=(70,'B')
C=(50,'F')
while True:
    scoer = (input("กรอกคะแนนของคุณ : "))
    if(scoer == "y"):
        print("จบการทำงาน")
        break
    elif float(scoer) >= A[0]:
        print('คะแนน :', scoer,"ได้เกรด :", A[1])
    elif float(scoer) >= B[0]:
        print('คะแนน :', scoer,"ได้เกรด :", B[1])
    elif float(scoer) < C[0]:
        print('คะแนน :', scoer,"ได้เกรด :", C[1])