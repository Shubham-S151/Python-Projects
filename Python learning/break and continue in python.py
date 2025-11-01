# break in python cause the loop to end at the particular condition
for i in range(1,13):
    print('5 X ',i,'=',5*i)
    if i==10:
        break
print('break cause the loop to end at i=10')
# continue in python cause the program to skip the particular iteration
for i in range(1,13):
    print(i,end=" ")
    if i==11:
        print('continue cause the loop to skip te 11th iteration')
        continue
    print("5 X",i,'=',5*i)
# another example of break statement
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print('mississipi')
print('break statement')