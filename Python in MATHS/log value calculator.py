import cmath
print("To make a simple log value calculator for values > 0")
a=input("enter your number:")
log10=cmath.log10(float(a))
log=cmath.log(float(a))
print("the value of log10 for given number is",log10)
print("the value of log for given number is",log)
r=(log/log10)
print("the relation between log10 and log is :",r)