import xlsxwriter
import math
print("Enter X of center point: ")
centerX = float(input())
print("Enter Y of center point: ")
centerY = float(input())
print("Enter X of zero degree point point: ")
zeroX = float(input())
print("Enter Y of zero degree point point: ")
zeroY = float(input())
print("Enter length between points (without scale): ")
lengthBetween = float(input())
print("Enter rotation side (clockwise: 1, anticlockwise: -1): ")
clockwiseNum = int(input())
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
plecy = open("plecy.txt", "r")
ugly = open("ugly.txt", "r")
vertical = open("verticalugly.txt", "r")
text_from_plecy = str(plecy.read()).splitlines()
text_from_ugly = str(ugly.read()).splitlines()
text_from_vertical = str(vertical.read()).splitlines()
A = zeroX - centerX
B = zeroY - centerY
def intToDeg(floatNum):
	jj = math.modf(float(floatNum))
	return float(jj[1] + round((jj[0]*100)/60, 2))
def arcPointCalc(theta):
	angle = intToDeg(theta)*3.14*clockwiseNum/180
	newpoint_x = cos(angle)*A + sin(angle)*B
	newpoint_y = -sin(angle)*A + cos(angle)*B
	X = centerX + newpoint_x
	Y = centerY + newpoint_y
	return [X, Y]
k = 1
print(arcPointCalc(270.56))
# def coordinateCalc(ugol, dlinna):
# 	if(lengthBetween < dlinna):
# 		lampda = lengthBetween/float(dlinna)
# 		thisAngle = arcPointCalc(ugol)
# 		finalX = (thisAngle[0]*(1+lampda) - centerX)/lampda
# 		finalY = (thisAngle[1]*(1+lampda) - centerX)/lampda
# 		return [finalX, finalY]
# 	else:
# 		lampda = float(dlinna)/lengthBetween
# 		thisAngle = arcPointCalc(ugol)
# 		finalX = (centerX + lampda*thisAngle[0])/(1+lampda)
# 		finalY = (centerY + lampda*thisAngle[1])/(1+lampda)
# 		return [finalX, finalY]
# print(coordinateCalc(intToDeg(text_from_ugly[0]), text_from_plecy[0]))
# km = input()
# while k <= len(text_from_ugly):
# 	worksheet.write('A'+str(k+1), coordinateCalc(DegToRad(intToDeg(text_from_ugly[k-1])), text_from_plecy[k-1])[0])
# 	worksheet.write('B'+str(k+1), coordinateCalc(DegToRad(intToDeg(text_from_ugly[k-1])), text_from_plecy[k-1])[1])
# 	k += 1
workbook.close()