#write a code that print all the sting after the comma 
names="khushi,achintya kumar rai"
index=0
for i in names:
    if i == ",":
        break
    index+=1
print(names[index+1:])
