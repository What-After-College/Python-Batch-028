# def sayhello(name):
#     return "hello "+name


# print(sayhello("adwaita"))


# def cTOf(c_temp):
#     return (9/5)*c_temp+32

# c_temp = float(input())
# print(cTOf(c_temp))

# n=int(input())
# fac=1
# for i in range(1,n+1):
#     fac*=i
# print(fac)

# def fact(n):
#     ans=1
#     for i in range(1,n+1):
#         ans*=i
#     return ans

# print(fact(5))


# def sayhello(name):
#     print(name)


# print(sayhello("adwaita"))


# import math

# print(math.ceil(5.1))
# print(math.floor(5.9))



# print(chr(69))
# print(ord('e'))

# print(max(92,95))
# print(min(6,5))



# lis = [1,2,3,4]
# print(len(lis))


# st="neeraj sharma"
# print(len(st))


# print(5**5)
# pow()



# def mul_return():
#     return 5,6

# a,b = mul_return()
# print(a,b)



def factorial(n):
    if n==1:
        return 1
    else:
        fac=factorial(n-1)*n
    return fac
        
print(factorial(5))




