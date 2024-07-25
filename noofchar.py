#code that print all the character of the sting and no of the charater present in it 
name=input("enter your name")
no_of_char=0
index=0
for i in name :
    print("the character",i,"is indexed at",index )
    no_of_char+=1
    index+=1
print("number of character in your name is ", no_of_char)