# program to greet 
import time
timestrap=(time.strftime('%H : %M: %S'))
print(timestrap)
timestrap1=int(time.strftime('%H'))
print(timestrap1)
timestrap2=int(time.strftime('%M'))
print(timestrap2)
timestrap3=int(time.strftime('%S'))
print(timestrap3)
hour=timestrap1
if (0<hour<12):
    print("good morning")
elif (12<hour<18) :
    print('good afternoon')
elif (18<hour<19):
        print('good evening')
else :
    print('good night')

# here int function converts 12 hrs time format to 24 hrs format