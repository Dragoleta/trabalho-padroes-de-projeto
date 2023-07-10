from complex_password_strategy import ComplexPasswordStrategy
from simple_password_strategy import SimplePasswordStrategy

class MenuPassword:
	def menu_password():
	#mover essa logica para uma file separada
		lenght = int(input('Tamanho da senha desejada: '))	
		tipo = str(input('Senha simples(1) ou complexa(2): '))
		
		match tipo:
			case '1':
				print('ok')
				simple_strategy = SimplePasswordStrategy()
				simple_strategy.generate_password(lenght)
			case '2':
				print('ok case 2')
				complex_strategy = ComplexPasswordStrategy()
				complex_strategy.generate_password(lenght)

