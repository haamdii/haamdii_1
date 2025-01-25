
# def call(*x):
#     a=0
#     for y in x:
#         a += y
#         print (a) 

# a = 5
# b= 2
# c= 9 
# d = 3

# call(a,b,c,d)

# while  True:
#     def factorial(n):
#         x = 0
#         while n >= 1:
#             x = x * n
#             n = n - 1
#         return x
#     print(factorial (int(input( '\n insert nymber :')))



def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return (x*fac(x-1))
print(fac(int(input( "Enter Number : "))))
        