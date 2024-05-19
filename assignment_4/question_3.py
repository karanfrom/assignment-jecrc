# 3. Write a Python function to find the maximum and minimum numbers in a given list of numbers without using 
# in built functions.

def maxmin(l):
    if not l:
        print("none")
    max=min=l[0]
    for i in l:
        if i>max:
            max=i
        elif i<min:
            min=i
    print("maximun number is:",max)
    print("minimun number is :",min)

lst=[12,13,45,99,1,34,65,23,64,23]
maxmin(lst)




