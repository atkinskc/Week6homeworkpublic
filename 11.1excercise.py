Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def word_check():
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		words = line.strip()
		d[words] = words
	return d

>>> word_check('abas')

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    word_check('abas')
TypeError: word_check() takes no arguments (1 given)
>>> def word_check():
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		words = line.strip()
		d[words] = words
	return words

>>> word_check('abas')

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    word_check('abas')
TypeError: word_check() takes no arguments (1 given)
>>> def word_check():
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		words = line.strip()
		d[words] = word
		if line not in d
		
SyntaxError: invalid syntax
>>> def word_check():
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		words = line.strip()
		d[words] = word
		if line not in d:
			print "false"
		else:
			print "True"
	return d

>>> word_check('abas')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    word_check('abas')
TypeError: word_check() takes no arguments (1 given)
>>> def word_check():
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		word = line.strip()
		d[words] = word
		if line not in d:
			print "false"
		else:
			print "True"
	return d

>>> word_check('abas')

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    word_check('abas')
TypeError: word_check() takes no arguments (1 given)
>>> word_check('abase')

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    word_check('abase')
TypeError: word_check() takes no arguments (1 given)
>>> def word_check(word):
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		word = line.strip()
		d[words] = word
	if word.find(word):
		return ('true')
	else:
		return ('false')

	
>>> word_check('abase')
'false'
>>> word_check('abas')
'false'
>>> word_check('the')
'false'
>>> def word_check(word):
	words = open("C:\Python27\words.txt")
	d = dict()
	for line in words:
		word = line.strip()
		d[words] = word
	if word.find(word) == -1:
		return ('true')
	else:
		return ('false')

	
>>> word_check('abas')
'false'
>>> word_check('abase')
'false'
>>> def word_check(word):
	fin = open("C:\Python27\words.txt")
	d = dict()
	for line in fin:
		word = line.strip()
		d[fin] = word
	if word.find(word) == -1:
		return ('true')
	else:
		return ('false')

	
>>> word_check(word)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    word_check(word)
NameError: name 'word' is not defined
>>> word_check('abase')
'false'
>>> word_check('abas')
'false'
>>> def word_check(word):
	fin = open("C:\Python27\words.txt")
	d = dict()
	count = 0
	for line in fin:
		word = line.strip()
		d[fin] = word
	if word.find(word) == -1:
		return ('true')
	else:
		return ('false')

	
>>> word_check('abas')
'false'
>>> word_check('abase')
'false'
>>> def word_check(word):
	fin = open("C:\Python27\words.txt")
	d = dict()
	for line in fin:
		word = line.strip()
		d[fin] = word
		if word in d:
			return ('True')
		if word not in d:
			return ('False')

		
>>> word_check('abas')
'False'
>>> word_check('Abase')
'False'
>>> word_check('Kennedy'0
	   
SyntaxError: invalid syntax
>>> word_check('Kennedy')
'False'
>>> def word_check(word):
	fin = open("C:\Python27\words.txt")
	d = dict()
	for word in fin:
		word = word.strip()
		d[fin] = word
		if word in d:
			return ('True')
		if word not in d:
			return ('False')

		
>>> 
>>> word_check('Kennedy')
'False'
>>> worD_check('True')

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    worD_check('True')
NameError: name 'worD_check' is not defined
>>> word_check('true')
'False'
>>> word_check(word)

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    word_check(word)
NameError: name 'word' is not defined
>>> def word_check(word):
	fin = open("C:\Python27\words.txt")
	d = dict()
	for line in fin:
		word = line.strip()
		d[fin] = word
		if word not in d:
			return ('False')
		else:
			return ('true')

		
>>> word_check('kennedy')
'False'
>>> word_check('abas')
'False'
>>> def word_check(word):
	fin = open("C:\Python27\words.txt")
	d = dict()
	for line in fin:
		word = line.strip()
		d[line] = word
		if word not in d:
			return ('False')
		else:
			return ('true')

		
>>> 
>>> word_check('abas')
'False'
>>> def word_check():
	fin = open("C:\Python27\words.txt")
	d = dict()
	for line in fin:
		word = line.strip()
		d[fin] = word
		if word not in d:
			return ('False')
		else:
			return ('true')

		
>>> word_check('abas')

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    word_check('abas')
TypeError: word_check() takes no arguments (1 given)
>>> def word_check(x):
	fin = open("C:\Python27\words.txt")
	d = dict()
	for line in fin:
		word = line.strip()
		d[fin] = word
		if word not in d:
			return ('False')
		else:
			return ('true')

		
>>> word_check('abas')
'False'
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if word not in d:
			return ('False')
		else:
			return ('true')

		
>>> word_check('abas')
'False'
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			return ('False')
		else:
			return ('true')

		
>>> word_check('abas')
'False'
>>> word_check('kennedy')
'False'
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if word not in d:
			d[fin] = 1
		else:
			d[fin] += 1
		return d

	
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[fin] = 1
		else:
			d[fin] += 1
		return d

	
>>> word_check('abas')
{<open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033865D0>: 1}
>>> word_check('kennedy')
{<open file 'C:\\Python27\\words.txt', mode 'r' at 0x0000000003386780>: 1}
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[fin] = 1
		else:
			d[fin] += 1
		return d

	
>>> word_check('abas')
{<open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033866F0>: 1}
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[x] = 1
		else:
			d[x] += 1
		return d

	
>>> word_check9'abas')
SyntaxError: invalid syntax
>>> word_check('abas')
{'abas': 1, <open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033865D0>: 'aa'}
>>> word_check('kennedy')
{'kennedy': 1, <open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033866F0>: 'aa'}
>>> 
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[x] = 0
		else:
			d[x] += 1
		return d

	
>>> word_check('abas')
{<open file 'C:\\Python27\\words.txt', mode 'r' at 0x0000000003386780>: 'aa', 'abas': 0}
>>> word_check('kennedy')
{'kennedy': 0, <open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033866F0>: 'aa'}
>>> word_check('abase')
{<open file 'C:\\Python27\\words.txt', mode 'r' at 0x0000000003386780>: 'aa', 'abase': 0}
>>> word_check('the')
{'the': 0, <open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033866F0>: 'aa'}
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[word] = 0
		else:
			d[word] += 1
		return d

	
>>> word_check('abas')
{'aa': 0, <open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033865D0>: 'aa'}
>>> word_check('kennedy')
{'aa': 0, <open file 'C:\\Python27\\words.txt', mode 'r' at 0x00000000033866F0>: 'aa'}
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[x] = 0
		else:
			d[x] += 1
		return d

	
>>> def word_check(x):
	d = dict()
	fin = open("C:\Python27\words.txt")
	for line in fin:
		word = line.strip()
		d[fin] = word
		if x not in d:
			d[x] = 0
		else:
			d[x] += 1
		return d

	
>>> 
