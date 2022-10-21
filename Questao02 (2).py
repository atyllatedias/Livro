ingrs: float 
qntingrs: int 
desp: int 
renda: float 
lucro: float

import os

ingrs = 5
desp = 200
qntingrs = 120

os.system("cls")

while ingrs >= 1:
    renda = ingrs * qntingrs
    lucro = renda - desp
    print(f"|O preço do ingresso é: \t\t    {ingrs:.1f} |")
    print(f"|A quantidade de ingressos vendidos é: \t    {qntingrs} |") 
    print(f"|O lucro com essa quantidade de ingressos é: {lucro:.1f}|")
    print("=" *49)
    qntingrs += 26
    ingrs -= 0.5