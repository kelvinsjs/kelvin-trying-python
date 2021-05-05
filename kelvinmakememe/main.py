from time import sleep
print('Я...', end='   ')
sleep(1)
print('ЖИГУЛЬ!')
for i in range(1000,6,-7):
	sleep(0.2)
	print(f'{i} - 7 = {i-7}')
	sleep(1)
	print('Я стал сильнее...', end = "   ")
	sleep(2)
	print('Но какой ценой?')