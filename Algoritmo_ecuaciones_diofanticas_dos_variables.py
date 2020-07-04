from sys import stdin
l1=[]
def euclides(num1,num2,iteracciones=1):
    l2=[]
    # Si el num1 es inferior al num2, los invertimos
    if num1<num2:
        num1,num2=num2,num1
     
    # obtenemos el residuo de la division
    resto=num1%num2
    cociente=num1//num2
    print("------------------------------")
    print(str(num1)+" "+"|_"+str(num2))
    print("r:",resto,"c:",cociente)
    print("------------------------------")
    l2.append(num1)
    l2.append(num2)
    l2.append(resto)
    l2.append(cociente)
    l1.append(l2)
    if resto==0:
        return (num2,iteracciones)
 
    # llamamos nuevamente a la función pasando como primer parametro el
    # segundo numero y el resto de la division
    return euclides(num2,resto,iteracciones+1) # -> Ecuación de recurrencia
    

print("numero a: ",end="") 
num1=int(stdin.readline())
print("numero b: ",end="") 
num2=int(stdin.readline())
print("numero n: ",end="") 
final=int(stdin.readline())
 
comunDivisor,iteracciones=euclides(num1,num2)
 
print("El común divisor de {} y {} es {}".format(num1,num2,comunDivisor))
print("Se ha encontrado en {} iteraciones".format(iteracciones))

for x in l1:
    print(str(x[0])+" = "+str(x[1])+"("+str(x[3])+") + "+str(x[2])+"(1)")

print("")
print(str(comunDivisor)+" = "+str(num1)+"(ß)"+" + "+str(num2)+"(æ)")
print(num1,"* (Introducir beta) : ",end="")
beta=int(stdin.readline())
print(num2,"* (Introducir alfa) : ",end="")
alfa=int(stdin.readline())
res=((num1)*(beta))+((num2)*(alfa))
print("")
if res==comunDivisor:
    print("x1,y1 para la solución x´,y´")
    x1=(final*beta)/comunDivisor
    y1=(final*alfa)/comunDivisor
    print("x1=",x1)
    print("y1=",y1)
    print("")
    print("x´= "+str(x1)+" + "+str((num2/comunDivisor))+"t")
    print("y´= "+str(y1)+" - "+str((num1/comunDivisor))+"t")
    print("")
    t1=(-1*x1)/(num2/comunDivisor)
    t2=y1/(num1/comunDivisor)
    print("t(x) >",((-1*x1)/(num2/comunDivisor)))
    print("t(y) >",((-1*y1)/((-1*num1)/comunDivisor)))
    print("")
    t1positiva=int(t1+1)
    t1negativa=int(t1-1)
    t2positiva=int(t2+1)
    t2negativa=int(t2-1)
    if ((t1positiva and t2positiva) > t1 and (t1positiva and t2positiva) > t2):
        tps=t1positiva+1
        xx=x1+((num2/comunDivisor)*tps)
        yy=y1-((num1/comunDivisor)*tps)
        print("Solución propuesta: "+str(tps)+" o enteros mayores t")
        print("")
        print("x´= "+str(x1)+" + "+str((num2/comunDivisor))+"("+str(tps)+")")
        print("x´= "+str(xx))
        print("")
        print("y´= "+str(y1)+" - "+str((num1/comunDivisor))+"("+str(tps)+")")
        print("y´= "+str(yy))
        print("")
        if num2 > 0:
            print(str(num1)+"("+str(xx)+")"+" + "+str(num2)+"("+str(yy)+")= "+str(final))
            print(str(num1*xx)+" + "+"("+str(num2*yy)+")"+" = "+str(final))
            print(str(int((num1*xx)+(num2*yy)))+" = "+str(final))
        else:
            print(str(num1)+"("+str(xx)+")"+" - "+str(num2)+"("+str(yy)+")= "+str(final))
            print(str(num1*xx)+" - "+"("+str(num2*yy)+")"+" = "+str(final))
            print(str(int((num1*xx)+(num2*yy)))+" = "+str(final))
    if ((t1negativa and t2negativa) > t1 and (t1positiva and t2positiva) > t2):
        tps=t1negativa-1
        xx=x1+((num2/comunDivisor)*tps)
        yy=y1-((num1/comunDivisor)*tps)
        print("Solución propuesta: "+str(tps)+" o enteros menores t")
        print("")
        print("x´= "+str(x1)+" + "+str((num2/comunDivisor))+"("+str(tps)+")")
        print("x´= "+str(xx))
        print("")
        print("y´= "+str(y1)+" - "+str((num1/comunDivisor))+"("+str(tps)+")")
        print("y´= "+str(yy))
        print("")
        if num2 > 0:
            print(str(num1)+"("+str(xx)+")"+" + "+str(num2)+"("+str(yy)+")= "+str(final))
            print(str(num1*xx)+" + "+"("+str(num2*yy)+")"+" = "+str(final))
            print(str(int((num1*xx)+(num2*yy)))+" = "+str(final))
        else:
            print(str(num1)+"("+str(xx)+")"+" - "+str(num2)+"("+str(yy)+")= "+str(final))
            print(str(num1*xx)+" - "+"("+str(num2*yy)+")"+" = "+str(final))
            print(str(int((num1*xx)+(num2*yy)))+" = "+str(final))
    
else:
    print("Alfa o beta no coinciden con el máximo común divisor de a y b")
