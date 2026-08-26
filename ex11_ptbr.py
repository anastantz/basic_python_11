# Programa que calcula a área de uma parede e a quantidade de tinta necessária

largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
tinta = area / 2

print(f"Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m².")
print(f"Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.")