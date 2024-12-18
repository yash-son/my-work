#File Handling
#In python file handling takes place in these 3 steps:
#Open fle
# Read or write File
#Close File

#There are two types of files

#Binary files
#to handle the bianry file we need to specify the software to open it

#Text files
#lines in a text file is termnated by a special character known as a end of a line.
#Text file is present in human redable form

#Open 
#To open or create a file in a python we use a open() method
#If the adress of the file is not given the file will created in the same directory
#where python file is present

#Various access modes in file hadling
#for text file
#r,w,a,r+(read or write),a+(read or append)

#For binary files
#rb,wb,ab,rb+,ab+

#Beffering is optional to include
"""Buffering is the process of storing a chunk of a
file in a temporary memory until the file loads
completely . In python there are different
values can be given. If the buffering is set to 0
, then the buffering is off . The buffering will be
set to 1 when we need to buffer the file."""

f=open('test.txt','w')

#close()
#to close and save the file handling

#writing information in a file
#write()
f=open('myfile.txt','w',1)
string="My name is yash"
f.write(string)
f.close()
#writelines(list)
l=['My name is yash.\n','i am doing btech']
f=open('m.txt','w')
f.writelines(l)
f.close()
#reading information from a file
'''
in 3 ways we can read
read(no. f characters)
readline()
readlines()
'''
#read()
f=open('myfile.txt','r',1)
text=f.read(5)
f.close()
print(text)

#readline()
#reads a line
#if one line is over it reads specified charaters of next line
f=open("myfile.txt",'r')
# r=f.read(5)
d=f.readline()
r=f.readline()
f.close()
print(r)

#readlines
#Reads all the lines in a text file inclsing end of line character
f=open('myfile.txt','r')
d=f.readlines()
f.close()
print(d)

#reading specific line in a 
ln=2
f=open("myfile.txt",'r')
s=f.readlines()
if (ln<=len(s)):
    print(s[ln-1].strip())
else:
    print('not founded')
f.close()


#append
f=open('myfile.txt','a+')
f.write("\nmy sister name is muskan.")
f.close()


#Writing in binary file
import pickle
myfile=open("s.txt",'wb')
dict={"name":"yash","age":56}
pickle.dump(dict,myfile)
myfile.close()

#reading from a binary file
import pickle 
myfile=open('t.txt','wb')
dict=[2,"Yash"]
pickle.dump(dict,myfile)
myfile.close()

import pickle
m=open('t.txt','rb')
s=pickle.load(m)
roll_no=s[0]
name=s[1]
print(f"Roll no: {roll_no},name: {name}")
m.close()