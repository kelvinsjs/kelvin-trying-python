def FindLabel([ID], [цинк], [свине], [Name], [нікел], [мідь], [манга]):
    output = " "
    if int([цинк]) > 200:
        output = str(" ".join([Name].split()[:3]))
        output = output + ".\n Рівень цинку: " + str([цинк])
    if int([свине]) > 1000:
        output = str(" ".join([Name].split()[:3]))
        output = output + ".\n Рівень свинцю: " + str([свине])
    if int([нікел]) > 100:
        output = str(" ".join([Name].split()[:3]))
        output = output + nameFactory + ".\n Рівень нікелю: " + str([нікел])
    if int([мідь]) > 200:
        output = str(" ".join([Name].split()[:3]))
        output = output + nameFactory + ".\n Рівень міді: " + str([мідь])
    return output
