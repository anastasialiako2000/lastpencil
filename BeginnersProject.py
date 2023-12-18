import string
import random
#2,3,4 totalpens  -> bot 1,2,3
#6,7,8 totalpens  -> bot 1,2,3
#10,11,12
#14,15,16
#18,19,20
totalpens= input("How many pencils would you like to use : ")
check = totalpens.isnumeric()

while (check == False):
    totalpens = input("The number of pencils should be numeric ")
    check = totalpens.isnumeric()

while(int(totalpens) <= 0):
    totalpens = input("The number of pencils should be positive ")
    check = totalpens.isnumeric()
    while (check == False):
        totalpens = input("The number of pencils should be numeric ")
        check = totalpens.isnumeric()

totalpens = int(totalpens)
x = "Anastasia"
y = "Fiona"
begins = input("Who will be the first (" + x + ", " + y + "): ")
while(begins!= "Anastasia" and begins!= "Fiona"):
    begins = input("Choose between 'Anastasia' and 'Fiona' ")
print(totalpens*"|")
while(totalpens != -1):
    if(begins == y):
        if((totalpens + 2)% 4 == 0):
            botans = 1
        elif((totalpens + 1) % 4 == 0):
            botans = 2
        elif(totalpens % 4 == 0):
            botans = 3
        else:
            botans = random.randrange(1,3)
            if(botans>totalpens):
                while(botans>totalpens):
                    botans = random.randrange(1,3)
        if(totalpens!=-1):
            print("Fiona's turn: ")
            print(botans)
            botans = int(botans)
        while(int(botans)== int(totalpens)):
            print("Anastasia won!")
            totalpens = -1
            break
        if(totalpens!=-1):
            totalpens -= botans
            print(totalpens*"|")
    else:
        ans = (input("Anastasia's turn! ")) #player enters a value
        check = ans.isnumeric()
        while(check==False): # if it is not a number
            ans = (input("Possible values: '1', '2' or '3' "))
            check = ans.isnumeric()
       # ans = int(ans)
        while(ans!= "1" and ans!= "2" and ans!= "3"):   # if it is not 1,2,3
            ans = (input("Possible values: '1', '2' or '3' "))
            check = ans.isnumeric()
        while(check==False): 
            ans = (input("Possible values: '1', '2' or '3' "))
            check = ans.isnumeric()

        ans = int(ans)

        while(int(totalpens) - int(ans) <0): #player enters many values
            ans = input("Too many pencils were taken ")

        while(int(ans)== int(totalpens)):
            print("Fiona won!")
            totalpens = -1
            break
        if(totalpens!= -1):
            totalpens = int(totalpens)
            totalpens -= int(ans)
            print(totalpens * "|")
    if (begins == x):
        begins = y
    else:
        begins = x
