# # # Calculator ucing try-except
# while True:
#     try:
#         def add(num1, num2):
#             return num1 + num2

#         def sub(num1, num2):
#             return num1 - num2

#         def mul(num1, num2):
#             return num1 * num2

#         def div(num1, num2):
#             return num1 / num2 

#         x = float(input( ' Entr nmbr 1 : '))
#         z = input( ' Press +, -, * or / : ')
#         y = float(input(' Entr nmbr 2 : '))
#         if z == '+' :
#             print("\n",add(x,y),"\n")
            
#         elif z == '-': 

#             print("\n",sub(x,y),"\n") 
#         elif z == '*': 

#             print("\n",mul(x,y),"\n")
#         elif z == '/':

#             print ("\n",div(x,y),"\n")    
#         else :
#             print("\n ERROR! PRESS '+', '-', '*' OR '/' AFTER ENTERING ONE NUMBER.\n ")
        
#         b = input("\n Type 'end' to end calculator, press other kye or enter for more :")     
#         if b == 'end':
#             print ( "\n THNX")
#             break  

#     except:
#         print("There may have some error(s)!! plz follow the instructions...\n ")

   

# number table
# while True:
#     def table(n, i=1):
#         if i>10:
#             return
#         print(n, "x", i, "=", n*i)
#         return table(n, i+1)

#     print("Enter the Number: ")
#     num = int(input())
   
#     table(num)  
#     print("\n")  

#     b = input("\nType 'n' to end, press other kye or enter for more :")     
#     if b == 'n':
#         print ( "\n THNX")
#         break  
# o = open( "text.txt", "r")
# p = open ("../Document.txt", "w")
# p.write( "helllo python hshsaa")
# p.close()
# q = open( "new text.txt", "x")

# import turtle 

# star = turtle.Turtle() 

# star.right(75) 
# star.forward(100) 

# for i in range(4): 
# 	star.right(144) 
# 	star.forward(100) 
	
# turtle.done() 


# importing the required module  
import datetime
print(datetime.datetime.now())