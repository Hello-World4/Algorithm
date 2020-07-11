def repeat(arr):
    "Find the maximum repeating number in list o(n^2)"
    max_repeat = 0
    result = 0
    for i in range(len(arr)):
        count = 0
        for j in range(i,len(arr)):
            if arr[i]==arr[j]:
                count +=1
            if count > max_repeat:
                max_repeat = count
                result = arr[i]
    return result,max_repeat

def reverse(str):
    return str[-1::-1]

def palindrome(str):
    return reverse(str) == str

def bruteForcetwoSum(arr,target):
  "Given an array of integers, return indices of the two numbers such that they add up to a specific target."
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        sum = arr[i] + arr[j]
        if sum == target:
            return i,j
  return -1

def twosum(arr,target): #o(n)
    dico = {}
    for i in range(len(arr)):
        result = target - arr[i]
        if arr[i] in dico:
            return [dico[arr[i]], i]
        else:
            dico[result] = i


def bubbleSort(arr): #o(n^2)
    drap = False
    while drap == False:
        drap = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                drap = False
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
    return arr

def facto(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return result;

def facto2(n):
    if n <= 1:
        return n
    return n * facto2(n-1)



def fibo(n): #iterative
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(n):
        c = a+b # 1 , 1
        a = b
        b = c
    return c


def fibo2(n):#not optimized
    if n <= 1:
        return n
    return fibo2(n-1) + fibo2(n-2)



def power(x,n): #iterative
    result = 1
    for i in range(n):
        result *=x
    return result

def power(x,n): #recursive
    " x^n = x * x^n-1"
    if n == 0:
        return 1
    return x * power(x, n-1)


if __name__ == "__main__":
    a = [20,7,40,1,3,2]
    str = "kayak"
    print(repeat(a))
    print(reverse(str))
    print(palindrome(str))
    print(bruteForcetwoSum(a,9))
    print(twosum(a,9))
    print(bubbleSort(a))
    print(facto2(5))
    print(facto(5))


    print(fibo(5))
    print(fibo2(5))
    print(power(2,4))
    print(power(2,4))