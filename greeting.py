import time 
t= int(time.strftime('%H'))
if t<12:
    print("good morning")
elif t==12:
    print ("good afternoon")
else :
    print("good night")
print("thank you, master")
