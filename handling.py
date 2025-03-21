file=open("football.txt",)
print(file.read())
file.close()

file=open("football.txt",'w')
file.write("I love football.")
file.close()

file=open("football.txt",'a')
file.write(" Do you love football ?")
file.close()