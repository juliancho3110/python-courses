#este es el hola mundo
print("Hello world")
print ("hola mundo")
#variables
name="Alicia"
age=20
note=3.8
active=True
print(name,type(name))
print(age,type(age))
print(note,type(note))
print(active,type(active))
#trabajando con variables
print(note+age)
print("hola " + name)
print("edad:"+str(age))
print(int("25")+age)
#operadores matematicos
print("adicion:",5+8)
print("resta:",5-8)
print("multiplicar:",5*8)
print("dividir:",5/8)
print("division entera:",5//8)
print("modulo:",5%8)
print("potencia:",5**8)
#operadores condicionales: siempre retornan a una variable booleana 
grade=3.8
print("=",grade==3.8) #todo lo que este escrito no se toma en cuenta 
print("diferente",grade!=3.8)# diferente
print(">=",grade>=3.8)#mayor o igual 
print("<",grade<3.8)#menor
print("<=",grade<=3.8) #menor o igual
print(">",grade>3.8)# mayor
#formato de string
print("edad:"+str(age))#aqui es concatenacion de strings
print(f"edad:{age}")# aqui es formato de string 
print(f"edad:{age}, nota: {grade}")# aqui es formato de string 