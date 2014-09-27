Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("Hello, World")
Hello, World
>>> 5+9
14
>>> abs(-63)
63
>>> help(abs)
Help on built-in function abs in module builtins:

abs(...)
    abs(number) -> number
    
    Return the absolute value of the argument.

>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.4's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> def convert_to_celcius(fahrenheit):
	return (fahrenheit - 32) * (5/9)

>>> 
>>> convert_to_celcius(32)
0.0
>>> convert_to_celcius(75)
23.88888888888889
>>> convert_to_celcius(79)
26.11111111111111
>>> def convert_to_milimeters(inches):
	""" (number) -> number

	returns the milimeters for an input of inches

	>>> convert_to_millimeters(2)
	50.8

	"""
	return inches * 25.4

>>> 
>>> convert_to_milimeters(2)
50.8
>>> help(convert_to_milimeters)
Help on function convert_to_milimeters in module __main__:

convert_to_milimeters(inches)
    (number) -> number
    
    returns the milimeters for an input of inches
    
    >>> convert_to_millimeters(2)
    50.8

>>> 
