print('Ноль в качестве знака операции завершит программу')
while True:
	s = input("Знак +, -, *, /: ")
	if s == '0':
		break
	if s in ('+', '-', '*', '/'):
		n1 = float(input('fist nomder= '))
		n2 = float(input('second nombeк= '))
		if s == '+':
			print(n1+n2)
		elif s == '-':
			print(n1-n2)
		elif s == '*':
			print(n1*n2)
		elif s == '/':
			if s != '0':
				print(n1/n2)
			else:
				print("На ноль делить нельзя, Карл!")
	else:
		print('Не верная операция')