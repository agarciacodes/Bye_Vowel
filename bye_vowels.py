Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def byevowel(string):
	words = list(string)
	new_string = []
	for i in words:
		if i.upper() == "A" or i.upper() == "E" or i.upper() == "I" or i.upper() == "O" or i.upper() == "U":
			pass
		else:
			new_string.append(i)
	return "".join(new_letters)

>>> 