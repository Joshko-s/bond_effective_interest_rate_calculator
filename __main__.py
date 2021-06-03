from math import isclose

def fetch_bondinfos():
	val = []
	print('Nominal value: ')
	nomval = input()
	print('Maturity: ')
	maturity = input()
	print('Price: ')
	price = input()
	print('Coupon rate: ')
	coupon = input()
	if coupon == None:
		print('Coupon: ')
		coupon = input()
	else:
		coupon = float(coupon) * float(nomval)
	val.append(float(nomval))
	val.append(int(maturity))	
	val.append(float(price))
	val.append(float(coupon))
	return val


def calculate(data1):
	rate = float(0.0001)
	price = float(data1[2])
	while True:
		rate = rate + float(0.0001)
		rbf = (1.0/rate)-(1.0/(rate*((1.0+rate)**data1[1])))
		equ = (rbf * data1[-1]) + (data1[0]/((1.0 + rate)**data1[1]))
		if isclose(price, round(equ, 2)):
			break

	return print('\n' + 'Effektive interest rate: ' + '\n' + str(round(rate, 6)) + '\n')


print('If there is no given coupon rate, enter: None.')
values = fetch_bondinfos()
calculate(values)