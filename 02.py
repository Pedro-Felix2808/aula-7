produto = "Mouse gamer WIFI"
valores = [20, 71, 100, 30]
alunos = ["Ana", "Hugo", "Mariana","Pedro", "Ana Paula"]

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
print(valores)   


aluno_procurado = input("Digite o nome do aluno que deseja: ")
alunos_encontrados = []
for aluno in alunos:
    alunos_encontrados.append(aluno)

print(alunos_encontrados)    

