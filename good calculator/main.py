file = open("calc.txt", "r")
text_from_file = file.read();
file.close()
complete = eval(text_from_file)
with open('calc.txt', 'w') as f:
	f.write("\n ******************************************* \n result: "+ str(complete) + " \n -------------------- finish ------------------")
	f.close()
print("done")