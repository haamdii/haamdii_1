# # full loop

# x = float(input( ' Entr nmbr 1 : '))
# z = input( ' Press +, -, * or / : ')
# y = float(input(' Entr nmbr 2 : '))


# if z == '+' :
#     print( "\n",x,z,y, "=" ,x + y )
# elif z == '-': 
#      print (  "\n",x,z,y, "=" ,x - y )
# elif z == '*': 
#      print (  "\n",x,z,y, "=" ,x * y)
# elif z == '/':
#      print (  "\n",x,z,y, "=" ,x / y)        
# else :
#     print("\n",'ERROR!') 

# b = input("\n \n type y for more, n to end :") 
# while not b == 'n':
#     while  b != 'y' and b != 'n':
#         print("\n PLZ FOLLOW INSTRUCTIONS")
#         b = input("\n \n type y for more, n to end :")
#     while b =='y':
#         x = float(input( 'Entr nmbr 1 : '))
#         z = input( ' Press +, -, * or / : ')
#         y = float(input( 'Entr nmbr 2 : '))
#         if z == '+' :
#             print( "\n",x,z,y, '=' ,x + y )
#         elif z == '-': 
#             print (  "\n",x,z,y, '=' ,x - y )
#         elif z == '*': 
#             print (  "\n",x,z,y, '=' ,x * y)
#         elif z == '/':
#             print (  "\n",x,z,y, '=' ,x / y)        
#         else :
#             print("\n",'ERROR!')
#         b = input("\n \n type y for more, n to end :")
   
    
# print('\n\nTHNXn\n\n')
   

# start func cal
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

x = float(input( ' Entr nmbr 1 : '))
z = input( ' Press +, -, * or / : ')
y = float(input(' Entr nmbr 2 : '))

if z == '+' :
    print("\n") 
    print(add(x,y))
elif z == '-': 
     print ("\n")
     print(sub(x,y)) 
elif z == '*': 
     print ("\n") 
     print(mul(x,y))
elif z == '/':
     print ("\n") 
     print ((div(x,y)))    
else :
    print("\n",'ERROR!')

b = input("\n \n type y for more, n to end :") 
while not b == 'n':
    while  b != 'y' and b != 'n':
        print("\n PLZ FOLLOW INSTRUCTIONS")
        b = input("\n \n type y for more, n to end :")
    while b =='y':
        x = float(input( 'Entr nmbr 1 : '))
        z = input( ' Press +, -, * or / : ')
        y = float(input( 'Entr nmbr 2 : '))
        if z == '+' :
            print("\n") 
        elif z == '-': 
            print ("\n")
            print(sub(x,y)) 
        elif z == '*': 
            print ("\n") 
            print(mul(x,y))
        elif z == '/':
            print ("\n") 
            print ((div(x,y)))    
        else :
            print(add(x,y))
            print("\n",'ERROR!')
        b = input("\n \n type y for more, n to end :")
   
    
print('\n\nTHNX\n\n')