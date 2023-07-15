Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
수강과목 = "한국사"; 내일시험일정 = ["국어", "한국사"]
if 수강과목 in 내일시험일정:
    print(수강과목+"를 공부하세요.")

    
한국사를 공부하세요.
나의정보 = [90, 1.6]
BMI = 나의정보[0] / (나의정보[1]*나의정보[1])
if BMI >= 25:
     print("비만입니다.")
... 
...      
비만입니다.
>>> BMI_1 = BMI; BMI_2 = 60/(1.6*1.6)
>>> if BMI_2 >= 25:
...     print("비만입니다.")
...     else:
...         
SyntaxError: invalid syntax
>>> if BMI_2 >= 25:
...     print("비만입니다.")
... else:
...     print("비만이 아닙니다.")
... 
...     
비만이 아닙니다.
>>> if BMI_2 >= 25:
...     print("비만")
... elif 23 <= BMI_2:
...     print("과체중")
... else:
...     print("비만 아님")
... 
...     
과체중
>>> if 4>3: "4는 3보다 크다!"
... 
'4는 3보다 크다!'
>>> box = 3
>>> "5보다 크다!" if box>5 else "5보다 작다!"
'5보다 작다!'
>>> "5보다 크다!" if box>5 else "3이다!" if a==3 else "..."
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    "5보다 크다!" if box>5 else "3이다!" if a==3 else "..."
NameError: name 'a' is not defined
>>> a = 3
>>> "5보다 크다!" if box>5 else "3이다!" if a==3 else "..."
'3이다!'
