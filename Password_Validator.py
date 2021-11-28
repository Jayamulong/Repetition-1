#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)

#Ask for users possible password
password = input("Insert password: ")

valid_Letter = 0
valid_Capital = 0
valid_Number = 0
valid_Char = 0

#Test if password have 15 letters
for i in range(0, len(password)):
    if password[i] != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14:
        valid_Letter = True

#Test if password have atleast one capital letter
for i in range(0, len(password)):
    if password[i] in ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"):
        valid_Capital = True

#Test if password have atleast one number
for i in range(0, len(password)):
    if password[i] in ('0',"1","2","3","4","5","6","7","8","9"):
        valid_Number = True

#Test if password have atleast one special character
for i in range(0, len(password)):
    if password[i] in ("!","@","#","$","%","^","&","*","(",")","_","+"):
        valid_Char = True
    
if valid_Letter == True:
    if valid_Capital == True:
        if valid_Number == True:
            if valid_Char == True:
                print("Valid") 
            else:
                print("Invalid")