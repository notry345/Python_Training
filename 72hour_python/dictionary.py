Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dictionary = {'Key' : 'Value', 'password' : 1234}
>>> dictionary[0]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dictionary[0]
KeyError: 0
>>> dictionary['Key']; dictionary['password']
'Value'
1234
>>> dictionary['Value']; dictionary[1234]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dictionary['Value']; dictionary[1234]
KeyError: 'Value'
>>> dictionary = {'Key' :}
SyntaxError: incomplete input
>>> dictionary = {:2}
SyntaxError: invalid syntax
>>> dictionry['python'] = 'is easy'
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dictionry['python'] = 'is easy'
NameError: name 'dictionry' is not defined. Did you mean: 'dictionary'?
>>> dictionary['python'] = 'is easy'
>>> dictionary
{'Key': 'Value', 'password': 1234, 'python': 'is easy'}
>>> dictionary['python'] = 'is hard'
>>> dictionary['C'] = 'is very hard'
>>> dictionary['list'] = [1,2,3]
>>> dictionary[1,2,3] = 'list2'
>>> dictionary[1] = 3
>>> dictionary
{'Key': 'Value', 'password': 1234, 'python': 'is hard', 'C': 'is very hard', 'list': [1, 2, 3], (1, 2, 3): 'list2', 1: 3}
