numusuario = input("Pon un número: ")
try:
    ival = int(numusuario)
except:
    ival = -1

if ival > 0 :
    print("Buen trabajo")
else:
    print("No es un número")
