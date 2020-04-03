import os

rep = input("Enter string to be replaced in filenames")
files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    new = f.replace(rep, '')
    os.rename(f,new)