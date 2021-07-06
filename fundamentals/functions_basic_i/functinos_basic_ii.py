def countdown(num):
    for i in range(num,-1,-1):
        print(i)
#countdown(5)

def print_and_return(arr):
    print(arr[0])
    return(arr[1])

def first_plus_length(arr):
    x = arr[0] + arr.length
    return x

def values_greater_than_second(arr):
    count = 0 
    arr2 = []
    if len(arr) == 1:
        #print("False")
        return False
    else:
        for i in range(len(arr)):
            if arr[i] > arr[1]:
                count+=1
                arr2.append(arr[i])
        print(count)
        return arr2

#values_greater_than_second([3])
#values_greater_than_second([5,2,3,1,4])

def length_and_value(x,y):
    arr = [] * x
    for i in range(x):
        arr.append(y)
    #print(arr)
    return arr

#length_and_value(4,7)
#length_and_value(6,2)