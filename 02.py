produto = "Mouse gamer WIFI"
valores = [20, 71, 100, 30]

if "mouse".lower() in produto.lower():
    print("produto encontado")

else: 
    print("produto nào encontado")   


def dobrar(valor):
    resultado = valor * 2
    return resultado

valore_novos= []
for valor in valores:
    valore_novos.append(dobrar(valor))    

print(valore_novos)
       
