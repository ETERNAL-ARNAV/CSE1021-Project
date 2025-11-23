#importing all the necessary modules to make the password generator
import pyfiglet
import random
import array as ar
from art import *

#The big interface
print("")
print("\t\t\t\t" + "="*63)
print("\t\t\t\t\t\tWELCOME TO THE PASSWORD GENERATOR")
print("\t\t\t\t" + "="*63)
print("")
#our password,initialized
password = ""

#for loop
i,j = 0,0
#declaring all the necessary variables for working
special_char = ar.array('w',['!','@','$','%','&','^','*','#','_','(',')','-','=','|','~',';','\'','\"',"\\",'/'])

#alphabet array
alphabet_lower_array = ar.array('w',['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

#number array
num_array = ar.array('i',[0,1,2,3,4,5,6,7,8,9,10])

#required functions
def capital(e):
    return(e.upper())
def addAlphabets_custom(password):
    random_num3 = random.randint(0,len(custom_array)-1)
    decide = random.randint(0,1)
    if decide==0:
        password = password + custom_array[random_num3].upper()
    else:
        password = password + custom_array[random_num3].lower()
    return(password)

def addAlphabets_random(password):
    random_num2 = random.randint(0,25)
    random_num3 = random.randint(0,1)
    if random_num3 == 0:
        password = password + alphabet_lower_array[random_num2]
    else:
        password = password + alphabet_upper_array[random_num2]
    return(password)

#using map function
alphabet_upper_array = map(capital,alphabet_lower_array)

#making of Capital array
ls1 = list(alphabet_upper_array)
alphabet_upper_array = ar.array('w',ls1)


ask = input("Do you want a random password or a custom password? Write R or C respectively.--->")
if ask=="R":
    ask1 = input("Do you want a weak password ,strong password or very strong password,enter W,S,VS respectively--->")

    #weak password
    if ask1=="W":
        passwordlen = 6
        while i<passwordlen and len(password)!=passwordlen:
            random_num1 = random.randint(1,7)
            if random_num1==1 or random_num1==4:
                random_num2 = random.randint(0,len(num_array)-1)
                password = password + str(num_array[random_num2])
            else:
               password = addAlphabets_random(password)
            i = i + 1
        print(password)

    #strong password
    elif ask1=="S":
        passwordlen = 8
        while i<passwordlen and len(password)!=passwordlen:
            random_num1 = random.randint(0,12)
            if random_num1==0 or random_num1 == 8 or random_num1 == 12 or random_num1 == 4 or random_num1 == 12:
                decide = random.randint(0,1)
                if decide==0:
                    random_num2 = random.randint(0,len(special_char)-1)
                    password = password + special_char[random_num2]
                else:
                    random_num2 = random.randint(0,len(num_array)-1)
                    password = password + str(num_array[random_num2])
            else:
                password = addAlphabets_random(password)
            i = i + 1
        print(password)
    
    #very strong password
    elif ask1=="VS":
        passwordlen=10
        while i<passwordlen and len(password)!=passwordlen:
            random_num1 = random.randint(0,12)
            if random_num1==0 or random_num1==4 or random_num1 == 8 or random_num1 == 12 or random_num1 ==2 or random_num1 == 10:
                decide = random.randint(0,1)
                if decide==0:
                    random_num2 = random.randint(0,len(special_char)-1)
                    password = password + special_char[random_num2]
                else:
                    random_num2 = random.randint(0,len(num_array)-1)
                    password = password + str(num_array[random_num2])
            else:
                password = addAlphabets_random(password)
            i = i + 1
        print(password)

    else:
        print("kindly enter input correctly and retry")

elif ask=="C":
    #custom array creation and ask for custom string
    ask3 = input("Enter the custom string--->")
    ls2 = []
    while i<len(ask3):
        char = ask3[i]
        ls2.append(char)
        i = i + 1
    custom_array = ar.array('w',ls2)
    ask4 = input("Do you want a weak password ,strong password or very strong password,enter W,S,VS respectively--->")

    #custom weak password
    if ask4 == 'W':
        passwordlen = 6
        if len(custom_array)==passwordlen:
            while j<2:
                random_num2 = random.randint(0,len(custom_array)-1)
                custom_array.pop(random_num2)
                j = j + 1
            i = 0
        while i<passwordlen and len(password)!=passwordlen:
            random_num2 = random.randint(0,6)
            random_num1 = random.randint(0,len(special_char) - 1)
            if random_num2==2 or random_num2==5:
                password = password + special_char[random_num1]
            else:
                password = addAlphabets_custom(password)
            i = i + 1
        print(password)

    #custom strong password
    elif ask4 == 'S':
        passwordlen = 8
        if len(custom_array)==passwordlen:
            while j<3:
                random_num2 = random.randint(0,len(custom_array)-1)
                custom_array.pop(random_num2)
                j = j + 1
        i = 0
        while i<passwordlen and len(password)!=passwordlen:
            random_num2 = random.randint(0,12)
            random_num1 = random.randint(0,len(special_char) - 1)
            if random_num2==0 or random_num2==4 or random_num2==8 or random_num2==12:
                password = password + special_char[random_num1]
            else:
                password = addAlphabets_custom(password)
            i = i + 1
        print(password)
            
        
    #custom very strong password
    elif ask4=="VS":
        passwordlen = 10
        if len(custom_array)==passwordlen:
            while j<5:
                random_num2 = random.randint(0,len(custom_array)-1)
                custom_array.pop(random_num2)
                j = j + 1
        i = 0
        while i<passwordlen and len(password)!=passwordlen:
            random_num2 = random.randint(0,12)
            random_num1 = random.randint(0,len(special_char) - 1)
            if random_num2==0 or random_num2==4 or random_num2==8 or random_num2==12 or random_num2==2 or random_num2==10:
                password = password + special_char[random_num1]
            else:
                password = addAlphabets_custom(password)
            i = i + 1
        print(password)
    else:
        print("kindly enter input correctly and retry")
else:
    print("kindly enter input correctly and restart the program")
