minutos = float(input("Informe quantos minutos foram consumidos: "))
if (minutos <= 200):
    minutos = (minutos*0.20)

if (minutos > 200 or minutos <= 400):
    minutos = (minutos *0.18)
else:
        minutos = (minutos* 0.15)
if (minutos > 800):
                minutos * 0.08
print("O valor a se pagar e: ", minutos)
