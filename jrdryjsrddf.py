
# Programa para calcular a media de um aluno

print("=== Calculadora de Media Escolar ===")

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("\n=== Resultado ===")
print(f"Aluno: {nome}")
print(f"Media final: {media:.2f}")

if media >= 7:
    print("Situacao: Aprovado!")
elif media >= 5:
    print("Situacao: Recuperacao!")
else:
    print("Situacao: Reprovado!")

