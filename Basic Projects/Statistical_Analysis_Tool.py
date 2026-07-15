# Project : Statistical Analysis Tool From Basics without Inbuilt Functions.
# this tool is going to calculate all basics metrics of statistics, 
# mean, median, sum, min, max, range, vaiance, std dev

# user input
def uinput():
    print("Welcome to EXcited Nulcei Basic Python Projects.")
    n = int(input("Please enter the size if data you want to enter: "))
    l = []
    for i in range(n):
        num = float(input(f"Enter Number {i+1}: "))
        l.append(num)
    return l

# min
def cmin(l:list, n:int):
    mn = l[0]
    for i in range(n):
        if mn > l[i]:
            mn = l[i]
    return mn

# max
def cmax(l:list, n:int):
    mn = l[0]
    for i in range(n):
        if mn < l[i]:
            mn = l[i]
    return mn

# sum
def csum(l:list):
    sm = 0
    for i in l:
        sm+=i
    return sm

# range
def crange(l:list):
    n = len(l)
    min, max = cmin(l,n), cmax(l,n)
    return max - min

# mean
def cmean(l:list):
    sm = csum(l)
    return sm/len(l)

# median
def csort(l:list, n:int):
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def cmedian(l:list, n:int):
    sl = csort(l,n)
    if n%2 == 0:
        idx0,idx1 = (n//2)-1 , (n//2) # if list has 6 elements then median is 
        # going to calculated from averaging 3,4 elements in python these are (2,3)idxs
        return (l[idx0]+l[idx1])/2
    else :
        return l[n//2]

# variance
def cvar(l:list, n:int):
    mn = cmean(l)
    sms = 0
    for i in range(n):
        temp = (mn - l[i])**2
        sms += temp
        # temp = 0
    return sms/n

# std dev
def std_dev(var):
    return var**(1/2)

# main execution
data = uinput()
n = len(data)

minimum = cmin(data, n)
maximum = cmax(data, n)
total = csum(data)
data_range = crange(data)
mean = cmean(data)
median = cmedian(data.copy(), n)  # use copy to avoid modifying original list
variance = cvar(data, n)
std = std_dev(variance)

print("\n" + "="*40)
print("        STATISTICAL ANALYSIS REPORT")
print("="*40)
print(f"Count           : {n}")
print(f"Sum             : {total}")
print(f"Minimum         : {minimum}")
print(f"Maximum         : {maximum}")
print(f"Range           : {data_range}")
print(f"Mean            : {mean}")
print(f"Median          : {median}")
print(f"Variance        : {variance}")
print(f"Standard Dev    : {std}")
print("="*40)