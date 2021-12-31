import os
import sys
folder = 'C:/Users/grisha/Downloads/delete me from this planet'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.png', '.jpg')
    output = os.rename(infilename, newname)