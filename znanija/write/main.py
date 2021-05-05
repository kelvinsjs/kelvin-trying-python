file = open("output3.txt", "w+")
file.write("hello")
openFile = open("input3.txt", "r")
data = openFile.readlines()
finalList = []
i = 0
associateList = ["unknown", "odin", "dva", "tri"]
print(len(associateList))
while i < len(associateList):
	if finalList[i] < len(associateList):
		file.write(associateList[i], "\n")
	else:
		file.write("unknown \n")
	i = i + 1
file.close()