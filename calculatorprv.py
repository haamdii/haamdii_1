x = float(input( ' Entr nmbr 1 : '))
z = input( ' Press +, -, * or / : ')
y = float(input(' Entr nmbr 2 : '))


if z == '+' :
    print( "\n",x,z,y, "=" ,x + y )
elif z == '-': 
     print (  "\n",x,z,y, "=" ,x - y )
elif z == '*': 
     print (  "\n",x,z,y, "=" ,x * y)
elif z == '/':
     print (  "\n",x,z,y, "=" ,x / y)        
else :
    print("\n",'ERROR!') 

b = input("\n \n type y for more, n to end :") 


while b!= 'y' and b!='n':
    print ('plz follow instructions')
    b = input( "\n\n type y for more, n to end :")
while b == 'y':
    x = float(input( 'Entr nmbr 1 : '))
    z = input( ' Press +, -, * or / : ')
    y = float(input( 'Entr nmbr 2 : '))
    if z == '+' :
        print( "\n",x,z,y, '=' ,x + y )
    elif z == '-': 
        print (  "\n",x,z,y, '=' ,x - y )
    elif z == '*': 
        print (  "\n",x,z,y, '=' ,x * y)
    elif z == '/':
        print (  "\n",x,z,y, '=' ,x / y)        
    else :
        print("\n",'ERROR!') 
b = input( "\n\n type y for more, n to end :")
while b == 'n':
    print('THNX')