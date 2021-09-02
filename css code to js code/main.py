ishodnik = open("ishodnik.txt", "r")
input_text = str(ishodnik.read()).replace('    ', '').replace(';', '",').replace(': ', ': "').splitlines()
final_array = []
for s in input_text:
	n = s.find('-')
	if n == -1:
		final_array.append(s)
		continue
	else: 
		final_array.append(s[:n] + (s[n+1]).upper() + s[n+2:])
final_array[-1] = final_array[-1].replace(",", "")
with open('final.txt', 'w') as f:
	for i in final_array:
		f.write(i + "\n")
print("Success!")