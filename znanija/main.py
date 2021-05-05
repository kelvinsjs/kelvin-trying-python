print("N = ")
a = int(input())
i = 0
while i <= a:
	i = i + 1
	if i%10 == 7:
		continue
	elif i%7 == int(0):
		continue
	else:
		print(i)