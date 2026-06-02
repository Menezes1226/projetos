anos=int(input("Digite o número de anos que fuma: "))
cigarros=int(input("Digite o número de cigarros fumados por dia: "))
valor=float(input("Digite o valor de um maço de cigarros: "))
total_cigarros=anos*365
valor_gasto=valor*total_cigarros
print(f"voce gastou: R$ {valor_gasto:.2f}")