peso: float
idadS50 = 0
alura150 = 0
idadS50ePeso60 =0
pRuivaSemA= 0
ruiva = 0
oioazul = 0

for n in range(1,7):
    idad= int(input("Digite idade: "))
    peso= float(input("Digite peso: "))
    altura= float(input("Digite altura: "))
    corDodOlho= input("Digite a cor dos olhos: ")
    cordocabelo= input("Digite a cor do cabelo ")
    
if idad > 50:
    if peso < 60:
        idadS50ePeso60 += 1
    else:
        idadS50 += 1
if altura < 1.50:
    alura150 += 1
if corDodOlho == "A":
    oioazul += 1
if cordocabelo == "R":
    if corDodOlho != "A":
        pRuivaSemA += 1
    else:
        ruiva += 1
    
print(f"A quantidade de pessoas com a idade superior a 50 anos e peso inferior a 60kg é: {idadS50ePeso60}")
print(f"A média de pessoas com altura inferior a 1,50m é de: {alura150/6}")
print(f"A porcentagem de pessoas com olhos azuis é: {oioazul/6*100}%")
print(f"A quantidade de pessoas ruivas que não possuem olho azul é de: {pRuivaSemA}")