ishodnik = open("ishodnik.txt", "r")
text_from_ishodnik = str(ishodnik.read()).splitlines()
step = 26.316
i = 0
with open('answer.txt', 'w') as f:
	while i < len(text_from_ishodnik):
		f.write(str(round(67000000 + float(text_from_ishodnik[i])*step, 3)) + "\n")
		i = i + 1
print("success!")

