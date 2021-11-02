Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:25:58) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	return d

>>> most_frequent('aaabbcccc')
{'a': 3, 'c': 4, 'b': 2}
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	return sorted(d)

>>> most_frequent('aaabbcccc''
	      
SyntaxError: EOL while scanning string literal
>>> most_frequent('aaabbcccc')
['a', 'b', 'c']
>>> def most_frequent(string):
	d = dict()
	for value in sorted(string):
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	return d

>>> most_frequent('aaabbcccc')
{'a': 3, 'c': 4, 'b': 2}
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	print sorted(string)

	
>>> most_frequent('abbccc')
['a', 'b', 'b', 'c', 'c', 'c']
>>> most_frequent('aaabbc')
['a', 'a', 'a', 'b', 'b', 'c']
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	a = sorted(d.items(), x: x[1], reverse = True)
	
SyntaxError: invalid syntax
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	a = sorted(d.items(), x: x[1], reverse = True)
	
SyntaxError: invalid syntax
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	a = t.sort(d)
	return a

>>> most_frequent('abbccc')

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    most_frequent('abbccc')
  File "<pyshell#26>", line 8, in most_frequent
    a = t.sort(d)
NameError: global name 't' is not defined
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	a = d.sort(d)
	return a

>>> most_frequent9('abbccc')

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    most_frequent9('abbccc')
NameError: name 'most_frequent9' is not defined
>>> most_frequent('abbcccc')

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    most_frequent('abbcccc')
  File "<pyshell#30>", line 8, in most_frequent
    a = d.sort(d)
AttributeError: 'dict' object has no attribute 'sort'
>>> def most_frequent(string):
	d = dict()
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1
	print sorted(d)

	
>>> most_frequent('aabbbcccc')
['a', 'b', 'c']
>>> def most_frequent(string):
	d = dict()
	for key in string:
		if key not in d:
			d[key] = 1
		else:
			d[key] += 1
	print sorted(d)

	
>>> most_frequent('aabbbcccc')
['a', 'b', 'c']
>>> def most_frequent(string):
	d = dict()
	for key in string:
		if key not in d:
			d[key] = 1
		else:
			d[key] += 1
	print sorted(string)

	
>>> most_frequent('aabbbcccc')
['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
>>> def most_frequent(string):
	d = dict()
	s = sorted(string, key = string.count, reverse = True)
	for value in string:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1

	return d

>>> most_frequent('aabbbcccc')
{'a': 2, 'c': 4, 'b': 3}
>>> ef most_frequent(string):
	d = dict()
	s = sorted(string, key=string.count, reverse=True)
	for value in s:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1

	return d
SyntaxError: invalid syntax
>>> 
>>> def most_frequent(string):
	d = dict()
	s = sorted(string, key=string.count, reverse=True)
	for value in s:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1

	return d

>>> most_frequent('aaaabbc')
{'a': 4, 'c': 1, 'b': 2}
>>> def most_frequent(string):
	d = dict()
	s = sorted(string,key=string.count,reverse=True)
	for value in s:
		if value not in d:
			d[value] = 1
		else:
			d[value] += 1

	return d

>>> most_frequent('aaaabbcccccccccccccccc')
{'a': 4, 'c': 16, 'b': 2}
>>> most_frequent('abbbcccc')
{'a': 1, 'c': 4, 'b': 3}

