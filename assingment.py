# # # table input (while)
# # a = int(input( 'Entr nmbr : '))
# # b = 1
# # while b <= 10:
# #   print(a,'X',b, '=', a * b)
# #   b += 1

# # # table input (for)
# # a = int(input( 'Entr nmbr : '))
# # b= range(1,11)
# # for c in b:
# #     print(a,'X',c, '=', a * c)

# # #calculator
# # x = float(input( ' Entr nmbr 1 : '))
# # z = input( ' Press +, -, * or / : ')
# # y = float(input(' Entr nmbr 2 : '))


# # if z == '+' :
# #     print( "\n",x,z,y, "=" ,x + y )
# # elif z == '-': 
# #      print (  "\n",x,z,y, "=" ,x - y )
# # elif z == '*': 
# #      print (  "\n",x,z,y, "=" ,x * y)
# # elif z == '/':
# #      print (  "\n",x,z,y, "=" ,x / y)        
# # else :
# #     print("\n",'ERROR!') 

# # b = input("\n \n type y for more, n to end :") 


# # while b!= 'y' and b!='n':
# #     print ('plz follow instructions')
# #     b = input( "\n\n type y for more, n to end :")
# # while b == 'y':
# #     x = float(input( 'Entr nmbr 1 : '))
# #     z = input( ' Press +, -, * or / : ')
# #     y = float(input( 'Entr nmbr 2 : '))
# #     if z == '+' :
# #         print( "\n",x,z,y, '=' ,x + y )
# #     elif z == '-': 
# #         print (  "\n",x,z,y, '=' ,x - y )
# #     elif z == '*': 
# #         print (  "\n",x,z,y, '=' ,x * y)
# #     elif z == '/':
# #         print (  "\n",x,z,y, '=' ,x / y)        
# #     else :
# #         print("\n",'ERROR!') 
# # b = input( "\n\n type y for more, n to end :")
# # while b == 'n':
# #     print('THNX')

# # calculator with fnctn

# # def add(num1, num2):
# #     return num1 + num2

# # def sub(num1, num2):
# #     return num1 - num2

# # def mul(num1, num2):
# #     return num1 * num2

# # def div(num1, num2):
# #     return num1 / num2

# # x = float(input(' Entr nmbr 1 : '))
# # z = input(' Press +, -, * or / : ')
# # y = float(input(' Entr nmbr 2 : '))


# # if z == '+' :
# #     print("\n") 
# #     print(add(x,y))
# # elif z == '-': 
# #      print ("\n")
# #      print(sub(x,y)) 
# # elif z == '*': 
# #      print ("\n") 
# #      print(mul(x,y))
# # elif z == '/':
# #      print ("\n") 
# #      print ((div(x,y)))    
# # else :
# #     print("\n",'ERROR!') 

# # b = input("\n \n type y for more, n to end :") 
# # while b!= 'y' and b!='n':
# #     print ('plz follow instructions')
# #     b = input( "\n\n type y for more, n to end :")
# # while b == 'y':
# #     x = float(input( ' Entr nmbr 1 : '))
# #     z = input( ' Press +, -, * or / : ')
# #     y = float(input(' Entr nmbr 2 : '))

# #     if z == '+' :
# #         print("\n") 
# #         print(add(x,y))
# #     elif z == '-': 
# #          print ("\n")
# #          print(sub(x,y)) 
# #     elif z == '*': 
# #          print ("\n") 
# #          print(mul(x,y))
# #     elif z == '/':
# #         print ("\n") 
# #         print ((div(x,y)))    
# #     else :
# #         print("\n",'ERROR!')
# #     b = input("\n\n type y for more, n to end :")

# # while b == 'n':
# #     print('THNX')

# # start func cal
# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2

# x = float(input( ' Entr nmbr 1 : '))
# z = input( ' Press +, -, * or / : ')
# y = float(input(' Entr nmbr 2 : '))

# if z == '+' :
#     print("\n") 
#     print(add(x,y))
# elif z == '-': 
#      print ("\n")
#      print(sub(x,y)) 
# elif z == '*': 
#      print ("\n") 
#      print(mul(x,y))
# elif z == '/':
#      print ("\n") 
#      print ((div(x,y)))    
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
#             print("\n") 
#             print(add(x,y))
#         elif z == '-': 
#             print ("\n")
#             print(sub(x,y)) 
#         elif z == '*': 
#             print ("\n") 
#             print(mul(x,y))
#         elif z == '/':
#             print ("\n") 
#             print ((div(x,y)))    
#         else :
#             print("\n",'ERROR!')
#         b = input("\n \n type y for more, n to end :")
   
    
# print('\n\nTHNX\n\n')
   
while True:
    try:
        def add(num1, num2):
            return num1 + num2

        def sub(num1, num2):
            return num1 - num2

        def mul(num1, num2):
            return num1 * num2

        def div(num1, num2):
            return num1 / num2 
    # while True:
        x = float(input( ' Entr nmbr 1 : '))
        z = input( ' Press +, -, * or / : ')
        y = float(input(' Entr nmbr 2 : '))
        if z == '+' :
            print("\n",add(x,y),"\n")
            
        elif z == '-': 

            print("\n",sub(x,y),"\n") 
        elif z == '*': 

            print("\n",mul(x,y),"\n")
        elif z == '/':

            print ("\n",div(x,y),"\n")    
        else :
            print("\n ERROR! PRESS '+', '-', '*' OR '/' AFTER ENTERING ONE NUMBER")
         

    except:
        print("There may have some error(s)!! plz follow the instructions...\n ")