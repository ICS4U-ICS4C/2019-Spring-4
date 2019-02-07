#write to file
fobject=open('im.txt','w')
fobject.write('hello hello') #write a single line
fobject.write('go\ngo\ngo\nstop') #write on separarte lines
fobject.close()

#read from file
#fobject=open('important.txt','r') #open .txt file for reading and assign it to an object, fobject
#print(fobject.read(5))#read how many bits (characters)
#print(fobject.read())#read the rest of the file
#fobject.close()

#read line-by-line
#fobject=open('important.txt','r') 
#print(fobject.readline())#read how many bits (characters)
#print(fobject.readlines())#read the rest of the file
#fobject.close()
