qt_rodas: int
peso_bruto: float
qt_pessoas: int

qt_rodas = int(input("informe a quantidade de rodas o seu veiculo tem: "))
peso_bruto = float(input("informe o peso bruto do seu veiculo: "))
qt_pessoas = int(input("informe a quantidade de pessoas: "))


if(qt_rodas == 2) or (qt_rodas == 3):
	print("A melhor Categoria pra sua habilitação é a : --- A ---.")

elif(qt_rodas >=4) and (qt_pessoas > 8):
	print("A melhor Categoria pra sua habilitação é a : --- D ---.")
	
elif(qt_rodas >=4) and (peso_bruto <= 3500) and (qt_pessoas <= 8):
	print("A melhor Categoria pra sua habilitação é a : --- B ---.")
	
elif(qt_rodas >=4) and (peso_bruto >3500) and (peso_bruto <= 6000):
	print("A melhor Categoria pra sua habilitação é a : --- C ---.")
	
elif(qt_rodas >=4) and (peso_bruto < 6000):
	print("A melhor Categoria pra sua habilitação é a : --- E ---.")
else:
	print("Infelizmente as especificação declaradas não permitem você ter uma habilitação !!! .")
