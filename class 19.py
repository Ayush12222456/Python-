file1=open("file.txt",r)
while True:
 line=file1.readline()
 if line=="":
      break

file1.close()