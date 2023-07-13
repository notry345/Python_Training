Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Complex = 17+1j
>>> IntBMI = 17
>>> FloatBMI = 17.0
>>> BinaryBMI = ob10001
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    BinaryBMI = ob10001
NameError: name 'ob10001' is not defined
>>> OctalBMI = 0o21
>>> HexademicalBMI = 0x11
>>> BinartyBMI = 0b10001
>>> Complex; IntBMI; FloatBMI; OctalBMI; HexademicalBMI
(17+1j)
17
17.0
17
17
>>> type(Complex);
<class 'complex'>
>>> type(IntBMI)
<class 'int'>
>>> type(FloatBMI)
<class 'float'>
>>> type(OctalBMI)
<class 'int'>
>>> type(HexademicalBMI)
<class 'int'>
>>> BinaryBMI = bin(17)
>>> OctalBMI = oct(17)
>>> HexademicalBMI = hex(17)
>>> BinaryBMI; OctalBMI; HexademicalBMI;
'0b10001'
'0o21'
'0x11'
>>> type(BinaryBMI)
<class 'str'>
>>> type(OctalBMI)
<class 'str'>
>>> type(HexademicalBMI)
<class 'str'>
