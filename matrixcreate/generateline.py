with open("txt.txt", "w") as file:
    for i in range(35):
        for k in range(72):
            file.write(f"{114 + i} \n")