거스름돈 = int(input("거스름돈: "))
만원 = 거스름돈//10000
money = 거스름돈-만원*10000
print("만원: "+str(만원)+"장")
오천원 = money//5000
money = money-오천원*5000
print("오천원: "+str(오천원)+"장")
천원 = money//1000
money = money-천원*1000
print("천원: "+str(천원)+"장")
오백원 = money//500
money = money-오백원*500
print("오백원: "+str(오백원)+"개")
백원 = money//100
money = money-백원*100
print("백원: "+str(백원)+"개")
오십원 = money//50
money = money-오십원*50
print("오십원: "+str(오십원)+"개")
십원 = money//10
print("십원: "+str(십원)+"개")
