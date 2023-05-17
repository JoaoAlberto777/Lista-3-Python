from Pilha import Pilha

def Convert_Dec(hexa):
    pilha = Pilha()

    for digito in hexa:
        pilha.insert(digito)
    
    expo = 0
    decimal =0
    while not pilha.is_empty(): 
        num = pilha.remove()
        if num.isdigit():
            decimal+= int(num) * (16 ** expo)
        else:    
            if num =="A":
                decimal+= 10 * (16 ** expo)
            elif num =="B":
                decimal+= 11 * (16 ** expo)
            elif num == "C":
                decimal+= 12 * (16 ** expo)  
            elif num == "D":
                decimal+= 13 * (16 ** expo) 
            elif num == "E":
                decimal+= 14 * (16 ** expo) 
            elif num == "F":
                decimal+= 15 * (16 ** expo)                                                           
        expo += 1        
    return decimal

Num_Hexa = input("Digite o número em Hexadecimal com letras MAIÚSCULAS(caso necessário): ")
print("Número em Hexadecimal: ",Num_Hexa)
Num_Dec = Convert_Dec(Num_Hexa)
print(f"O Elemento {Num_Hexa} em decimal é: ",Num_Dec)