#this prints out the text "hello world"
print("hello world")

#this is a variable. its a String they use words/characters
#you can use = to define the variable
Test_Var = "this is a Test Var that can be changed"

#Prints the Test_Var
print(Test_Var)

#this changes the variable
#it also makes it a equation 8 divided by 2 which equals 4
Test_Var = 8/2

#prints the Test_Var again to show the diffrence
print(Test_Var)

#you can also format the code like this
print(f"8 divided by 2 is {Test_Var}")
#f = format
#"is the words" & the {} denote the variable to be put into the words

#integers
age = 25

print(f"you are {age}")
      
age = age + 1

print (f"you are one year older your now {age}")

#floats (integers with decimals)
price = 19.99

print(f"the price is ${price}")

#boolean now

has_game = True
#most times used internally
#ignore the function i already knew how to do that
def Do_you_have_game():
    if has_game:
        print("you own the game")
    else:
        print(f"you need to pay ${price}")

Do_you_have_game()
#now change it
has_game = False
Do_you_have_game()