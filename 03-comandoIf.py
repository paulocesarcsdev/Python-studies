vl = int(input("Qual e a velociade do carro: "))

if vl  >= 110:
    print("Esta acima da velocidade o valor da multa e ", vl )
    vl = (vl - 110);
    vl = (vl*5);
    print("O valor da multa e", vl)
 if vl <= 110:
    print("Está na velocidade normal", vl)

    
