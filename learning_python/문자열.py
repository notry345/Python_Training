Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Hello!
SyntaxError: incomplete input
Hello
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined
"Hello!"
'Hello!'
'Hello!'
'Hello!'
'''
Hello!
'''
'\nHello!\n'
A = "Hello World!"
A
'Hello World!'
A[1]
'e'
A[0]
'H'
A[0:4]
'Hell'
A[0:5]
'Hello'
A[1:]; A[:4]
'ello World!'
'Hell'
A.find(Hello)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    A.find(Hello)
NameError: name 'Hello' is not defined
Hello = 'Hello'
A.find(Hello)
0
Hello = 'Hell'
A.find(Hello)
0
Hello = 'Hel'
A.find(Hello)
0
find_var = 'e'
A.find(find_var)
1
find_var = '1'
A.find(find_var)
-1
find_var = 'l'
A.find(find_var)
2
입력 방식 1 = '"따옴표로 문자열임을 알리고, 쌍따옴표로 말하는 중"'
SyntaxError: invalid syntax
입력방식1 = '"따옴표로 문자열임을 알리고, 쌍따옴표로 말하는 중"'
>>> 입력방식2 = "'쌍따옴표로 문자열임을 알리고, 따옴표로 생각하는 중'"
>>> 입력방식3 = '''
... 그는 생각했다
... '어라  따옴표를 3개씩 쓰니, 1개를 쓸 수 있네?'
... '''
>>> 입력방식4 = """
... 그렇다면
... "이렇게 할 수도"
... '이렇게 생각 할 수도 있구나'
... """
>>> print(입력방식1)
"따옴표로 문자열임을 알리고, 쌍따옴표로 말하는 중"
>>> print(입력방식2)
'쌍따옴표로 문자열임을 알리고, 따옴표로 생각하는 중'
>>> print(입력방식3)

그는 생각했다
'어라  따옴표를 3개씩 쓰니, 1개를 쓸 수 있네?'

>>> print(입력방식4)

그렇다면
"이렇게 할 수도"
'이렇게 생각 할 수도 있구나'

>>> A = "안녕"
>>> B = "하세요"
>>> A+B
'안녕하세요'
>>> "*"*5
'*****'
>>> A = "20180901.txt"
>>> B = "20180902.txt"
>>> "이 파일은 "+A[:4] + "년 "+A[4:6]+"월 "+A[6:8]+"일에 만들어진 "+A[9:]+"포맷의 파일입니다."
'이 파일은 2018년 09월 01일에 만들어진 txt포맷의 파일입니다.'
>>> "이 파일은 %s년 %s월 %s일에 만들어진 %s 포맷의 파일입니다."%(A[:4],A[4:6],A[6:8],A[9:])
'이 파일은 2018년 09월 01일에 만들어진 txt 포맷의 파일입니다.'
