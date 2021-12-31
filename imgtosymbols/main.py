from PIL import Image
import numpy


img = Image.open('test.jpg')
photo = img.convert('L')
width = photo.size[0] #define W and H
height = photo.size[1]
new_height = 30
new_width  = round(new_height * width / height)
imgLast = photo.resize((new_width, new_height), Image.ANTIALIAS)
pixelArray = []

for y in range(0, new_height): #each pixel has coordinates
    newArray = []
    for x in range(0, new_width):
        RGB = abs((10*round((imgLast.getpixel((x, y))*100)/2550))-100)
        newArray.append(RGB)
    pixelArray.append(newArray)

fillers = [" ", ".", "'", ";", "c", "x", "O", "K", "X", "W", "M"]
fillerNum = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

finalText = ""

testI = 0
while testI < len(pixelArray):
	if testI%4 != 0:
		print(pixelArray[testI])
		for k in pixelArray[testI]:
			jjj = 0
			while jjj < len(fillerNum):
				if (k == fillerNum[jjj]):
					finalText = finalText + fillers[jjj]
					jjj = jjj + 110
				else:
					jjj = jjj + 1
		finalText = finalText + "\n"
		testI = testI + 1
	else:
		testI = testI + 1

with open('img.txt', 'w', encoding="utf-8") as f:
	f.write(finalText)
	f.close()

print("Done!")
