num = input("Ingresa un numero Binario : ")
str(num)
number = 0
tam=len(num)-1
correct= True
if(correct):
  for i in range(0,len(num)):
    if(num[i]!='1'and num[i]!='0'):
      print("No es un numero Binario!!")
      break
  else:
    for i in range(0,len(num)):
      if(num[i]=='1'):
        number+=2**tam
      tam-=1

print("Numero Decimal = ",number)
