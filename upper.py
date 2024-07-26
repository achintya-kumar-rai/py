#write a code to convert name that start with a in the list to the upper case and print it 
l=[]
for i in range(4):
    name =input("enter the name")
    l.append(name)
print("list of the name are",l)
for i in l:
    if i[0]=="a" or i[0]=="A":
        print(i.upper())
