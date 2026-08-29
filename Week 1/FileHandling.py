# This file is to learn file handling 
file=open('File.txt','r')
print(file.read())
file.close()
writeData=input("Enter what you want to write intot the file")
file=open('File.txt','w')
file.write(writeData)
file.close()