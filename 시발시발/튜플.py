Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_info = ('ABC', 56, 167)
>>> my_info
('ABC', 56, 167)
>>> my_info[1]
56
>>> my_info[0]
'ABC'
>>> my_info[1:3]
(56, 167)
>>> my_info[1:]
(56, 167)
>>> my_info[1] = 59;
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    my_info[1] = 59;
TypeError: 'tuple' object does not support item assignment
>>> my_info_feb = ('ABC', 59, 169)
>>> my_info_jan = ('ABC', 56, 169)
>>> my_info_2months = (my_info_jan, my_info_feb); my_info_2months
(('ABC', 56, 169), ('ABC', 59, 169))
>>> my_info_2months
(('ABC', 56, 169), ('ABC', 59, 169))
>>> my_info_2months = [my_info_jan, my_info_feb]
>>> my_info_2months
[('ABC', 56, 169), ('ABC', 59, 169)]
