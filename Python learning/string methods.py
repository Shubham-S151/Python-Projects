# methods here reffers to the changes in strings
# below shows first modification in string that is upper() this function converts the letter to upper case
name="Shubham"
print(name.upper())
# strings are immutable so when we do some modifications it gives new string
# there are also a function that converts the letters of strings in lower case i.e, lower()
print(name.lower())
# next is rstrip() it only removes the trailing characters(that is the characters at the end of string)
a="hello!!!"
print(a.rstrip('!'))
print(a.rstrip('l'))
print(name.rstrip('m'))
# next method is replace() it replaces all occourences of a strin with other string
print(a.replace("hello","hazard"))
# next method is split it splits the string and convert it into a list 
b="bio hazard"
print(b.split(" "))#this splits b at the spaces 
b1="bio+hazard"
print(b1.split("+"))
# next is capitalize() it convert string first letter to upper case 
print(b.capitalize())
# next method is center() it aligns the strin to center as per the parameter given
print(name.center(50))
# note 
print(len(name))
print(len(name.center(50)))
print(name.center((50),"-"))
# next is count() it tells that how many times the letter in a string is repeated
print(name.count("h"))
# next is endswith() it checks that if a string end with a given value. if yes than gives true, else false
print(a.endswith("!"))
print(a.endswith("!!"))
print(a.endswith("!!!"))
print(b.endswith("!!!"))
n="my name is shubham"
print(n.endswith("is",0,10))
print(n.endswith("is",0,15))
# next is find() this method searches for the first occourence of the givejn value. if value is absent then gives -1 as result
print(n.find("is"))
# next method is index() it is same as endswith() but when substring is absent then it throws an exception
# print(n.index("ish")) #it gives error in output as: error substrin not found
print(n.index("is"))
# next method is isalnum() this returns true only if the entire string only consists A-Z,a-z,0-9.
# if any othe punctuations are presents than gives false
n1='welcometotheconsole'
n2='welcome to the console'
print(n1.isalnum())
print(n2.isalnum())
# next method is isalpha() and this returns true only if the entire string consists of A-Z,a-z,
# if any othe punctuations are presents than gives false
print(name.isalpha())
print(a.isalpha())
# next method is islower() it returns true only if the whole string consists of lower case 
print(b.islower())
print(name.islower())
# next method is isprintable() it returns true if the string is printable and false if not printable
a1='hello\n'
print(a.isprintable())
print(a1.isprintable())
# next method is isspace() this method returns true if and only if the string contains white spaces else false
x=' '
x1='    '
print(x.isspace())
print(x1.isspace())
# next method is istitle() this method returns true only if first letter of each word is capital in a string else returns false
print(name.istitle())
print(a.istitle())
# next method is isupper() this checks weather the string contains all upper case letters if so the returns true else false
print(name.isupper())
# next methos is startswith() this checks that weather the string starts with a word or not if yes then gives true else false 
print(n.startswith("my"))
print(n.startswith("is"))
# next method is swapcase() this method converts the letters in the strings from lower to upper and upper to lower in a string
print(name.swapcase())
# next method is title() this converts all the first letters of each words to upper case 
print(n.title())