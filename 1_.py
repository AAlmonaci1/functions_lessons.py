# # functions are way to wrap your code
# # into reuseable units

# #This is how u define a function
# #ONLY DO THIS ONCE
# #whatever I pass inside the paranthesis 
# #it's called a parameter(placeholder for future info)
# def sayHello(name, age, email):
#     print(f"say hello {name}")
#     print("Hello Governor")
#     print("welcome back")
#     print(f"your age is {age}")
#     print(f"your email is {email}")
# # once you define a function
# # you must call or invoke the function
# # when I pass info into the called function, it's called an argument
# sayHello("Michelle", 12, "mmichelle33@gmail.com") #since there is two, it repeats twice but with it's new name
# sayHello("Abi", 17, "aalmonaci1@gmail.com")

# def  determineEligibility(age):
#     # if your age is over 18, you can vote, otherwise you can't
#     if age >= 18:
#         print("you can vote")
#     else:
#         print("you have to wait")

# determineEligibility(12)
# determineEligibility(17)
# determineEligibility(19)

# def willYouGraduate(GPA, Credits, SAT):
#     #GPA and credits will be num value
#     #passed SAT will be boolean
#     if (GPA == 3.0) and (Credits >= 28) and (SAT == True):
#         print("You passed! Good luck in college")
#     elif (GPA < 3.0) or (Credits < 28) or (SAT == False):
#         print("back to the drawing board")
#     else:
#         print("talk to your counselor")

# willYouGraduate(2.8, 15, True)
# willYouGraduate(3.0, 27, True)
# willYouGraduate(3.0, 28, True)

############### return statements ###############

# return = statement used to end a function and send a result back to the caller
def add(x, y):
    z= x + y
    return z
def subtract(x, y):
    z= x - y
    return z
def multiply(x, y):
    z= x * y
    return z
def divide(x, y):
    z= x / y
    return z
#return ends a function, they won't print until you invoke

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + "" + last
full_name = create_name("spongebob", "squarepants")
print(full_name)
