my_file = open("some.txt", "r")
a = my_file.read()
print()
lst = a.replace('\x16	', '').split()
b = ""
i = 0
while i < len(lst):
	b = b + lst[i] + "; "
	i = i + 1
with open('answer.txt', 'w') as f:
	f.write(b)
	f.close()
print("Done :)")