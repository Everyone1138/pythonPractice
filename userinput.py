# here we have user input and how it works. 
def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"
    
user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))



user_input2 = input("Enter your name: ") # this is how you direct the input from a user into what you need it to go to 
surname = input("What is your surname: ")

message = "Hello %s %s!" % (user_input2, surname)
message2 = "Hello {} {}!".format(user_input2, surname) 
print(message)
print(message2)