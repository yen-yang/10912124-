''' main '''
# 使用自建的套件 myMath 來計算使用者輸入的五個數的平均值
from cbMath import myArithmetic,myCalcArea,myStatistics

a = int(input("輸入數字"))

b = int(input("輸入數字"))

c = int(input("輸入數字"))

d = int(input("輸入數字"))

e = int(input("輸入數字"))

x = (a,b,c,d,e)

print("平均值為",myStatistics.myMean(x))
