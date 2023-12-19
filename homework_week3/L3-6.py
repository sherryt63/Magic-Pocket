grade=int(input())
if(grade<60):
    rank="不合格"
elif(grade>=60 and grade<=74): #python中用【and】表示"与"
    rank="合格"
elif(grade>=75 and grade<=89):
    rank="良好"
else:
    rank="优秀"
print(rank)