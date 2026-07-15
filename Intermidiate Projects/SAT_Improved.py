# Project : Statistical Analysis Tool From Basics without Inbuilt Functions.
# this tool is going to calculate all basics metrics of statistics, 
# mean, median, sum, min, max, range, vaiance, std dev

# user input
def uinput():
    print("Welcome to Excited Nulcei Basic Python Projects.")
    n = int(input("Please enter the size of data you want to enter: "))
    l = []
    for i in range(n):
        num = float(input(f"Enter Number {i+1}: "))
        l.append(num)
    return l

# min
def cmin(l:list):
    mn = l[0]
    for i in range(len(l)):
        if mn > l[i]:
            mn = l[i]
    return mn

# max
def cmax(l:list):
    mn = l[0]
    for i in range(len(l)):
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
    min, max = cmin(l), cmax(l)
    return max - min

# mean
def cmean(l:list):
    sm = csum(l)
    return sm/len(l)

# median
def csort(l:list):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def cmedian(l:list):
    n = len(l)
    sl = sorted(l)
    if n%2 == 0:
        idx0,idx1 = (n//2)-1 , (n//2) # if list has 6 elements then median is 
        # going to calculated from averaging 3,4 elements in python these are (2,3)idxs
        return (sl[idx0]+sl[idx1])/2
    else :
        return sl[n//2]

# variance
def cvar(l:list):
    mean_val = cmean(l)
    return sum((x-mean_val)**2 for x in l)/len(l)

# std dev
def std_dev(var):
    return var**(1/2)

# main execution
def main():
    data = uinput()
    if len(data)==0:
        print("Data is Empty")
        return 0
    n = len(data)

    minimum = cmin(data)
    maximum = cmax(data)
    total = csum(data)
    data_range = crange(data)
    mean = cmean(data)
    median = cmedian(data.copy())  # use copy to avoid modifying original list
    variance = cvar(data)
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

main()