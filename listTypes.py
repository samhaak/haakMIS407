Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """ Data collections
"""
' Data collections\n'
>>> [1,2,3]
[1, 2, 3]
>>> {"a","e","i","o","u"}
{'e', 'o', 'u', 'a', 'i'}
>>> vowels = {"a","e","i","o","u"}
>>> print vowels
SyntaxError: invalid syntax
>>> print vowels:
	
SyntaxError: invalid syntax
>>> print "vowels"
SyntaxError: invalid syntax
>>> type(vowels)
<class 'set'>
>>> vowels.add("y")
>>> vowels
{'e', 'o', 'i', 'y', 'u', 'a'}
>>> vowels
{'e', 'o', 'i', 'y', 'u', 'a'}
>>> vowels.length
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    vowels.length
AttributeError: 'set' object has no attribute 'length'
>>> vowels.remove("y")
>>> vowels
{'e', 'o', 'i', 'u', 'a'}
>>> vowels.add("y")
>>> vowels
{'e', 'o', 'i', 'y', 'u', 'a'}
>>> mytuple = (1,2,3)
>>> type(mytuple)
<class 'tuple'>
>>> my3 = (1,2,3)
>>> my3
(1, 2, 3)
>>> type(my3)
<class 'tuple'>
>>> newtuple = (1)
>>> type(newtuple)
<class 'int'>
>>> newtuple.add(2,3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    newtuple.add(2,3)
AttributeError: 'int' object has no attribute 'add'
>>> newtuple = (1, )
>>> type(newtuple)
<class 'tuple'>
>>> newtuple
(1,)
>>> newtuple.add(2,3)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    newtuple.add(2,3)
AttributeError: 'tuple' object has no attribute 'add'
>>> for myindex in mytuple:
	print(myindex)

	
1
2
3
>>> Joe = ["joe",101]
>>> type(Joe)
<class 'list'>
>>> emp = (["joe",101],["jane",102],["jack",103])
>>> type(emp)
<class 'tuple'>
>>> emp[0]
['joe', 101]
>>> emp[0][0]
'joe'
>>> empNames = {"joe","jane","jack"}
>>> type(empNames)
<class 'set'>
>>> empDict = {"joe": 101, "jane": 102,"jack": 103}
>>> empDict
{'jane': 102, 'jack': 103, 'joe': 101}
>>> type(empDict)
<class 'dict'>
>>> for index in empDict:
	print(index, empDict[index])

	
jane 102
jack 103
joe 101
>>> empDict.keys()
dict_keys(['jane', 'jack', 'joe'])
>>> empDict.values()
dict_values([102, 103, 101])
>>> empDict.items()
dict_items([('jane', 102), ('jack', 103), ('joe', 101)])
>>> 
