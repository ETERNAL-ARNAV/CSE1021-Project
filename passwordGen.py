#importing all the necessary modules to make the password generator
import math
import random
import array as ar

#our password,initialized
password = ""

#for loop
i = 0
#declaring all the necessary variables for working
special_char = ar.array('w',['!','@','$','%','&','^','*','#','_','(',')','-','=','|','~',';','\'','\"',"\\",'/'])

#alphabet array
alphabet_lower_array = ar.array('w',['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

#capitalizing function for map method
def capital(e):
    return(e.upper())

#using map function
alphabet_upper_array = map(capital,alphabet_lower_array)

#making of Capital array
ls1 = list(alphabet_upper_array)
alphabet_upper_array = ar.array('w',ls1)


ask = input("Do you want a random password or a custom password? Write R or C respectively.")
if ask=="R":
    ask1 = input("Do you want a weak password ,strong password or very strong password,enter W,S,VS respectively")

    #weak password
    if ask1=="W":
        passwordlen = 6
        while i<passwordlen:
            random_num1 = random.randint(1,7)
            if random_num1==1 or random_num1==4:
                random_num2 = random.randint(0,len(special_char)-1)
                password = password + special_char[random_num2]
            else:
                random_num2 = random.randint(0,25)
                random_num3 = random.randint(0,1)
                if random_num3 == 0:
                    password = password + alphabet_lower_array[random_num2]
                else:
                    password = password + alphabet_upper_array[random_num2]
            i = i + 1
        print(password)

    #strong password
    elif ask1=="S":
        passwordlen = 8
        while i<passwordlen:
            random_num1 = random.randint(0,12)
            if random_num1==0 or random_num1==4 or random_num1 == 8 or random_num1 == 12:
                random_num2 = random.randint(0,len(special_char)-1)
                password = password + special_char[random_num2]
            else:
                random_num2 = random.randint(0,25)
                random_num3 = random.randint(0,1)
                if random_num3 == 0:
                    password = password + alphabet_lower_array[random_num2]
                else:
                    password = password + alphabet_upper_array[random_num2]
            i = i + 1
        print(password)
    
    #very strong password
    elif ask1=="VS":
        passwordlen=10
        while i<passwordlen:
            random_num1 = random.randint(0,12)
            if random_num1==0 or random_num1==4 or random_num1 == 8 or random_num1 == 12 or random_num1 ==2 or random_num1 == 10:
                random_num2 = random.randint(0,len(special_char)-1)
                password = password + special_char[random_num2]
            else:
                random_num2 = random.randint(0,25)
                random_num3 = random.randint(0,1)
                if random_num3 == 0:
                    password = password + alphabet_lower_array[random_num2]
                else:
                    password = password + alphabet_upper_array[random_num2]
            i = i + 1
        print(password)

    else:
        pass
    